import json
import requests
from config import (
    OPENAI_API_KEY,
    USE_OLLAMA,
    OLLAMA_URL,
    OLLAMA_MODEL,
    USE_GROQ,
    GROQ_API_KEY,
    GROQ_MODEL,
    USE_MISTRAL,
    MISTRAL_API_KEY,
    MISTRAL_MODEL,
    MISTRAL_API_URL,
)

class LLMExtractor:
    def __init__(self):
        self.use_ollama = USE_OLLAMA
        self.use_groq = USE_GROQ
        self.use_mistral = USE_MISTRAL
        
    def check_connection(self) -> bool:
        """Vérifie si le service LLM configuré est accessible."""
        print("🔍 Vérification du service LLM...")
        
        if self.use_groq:
            if not GROQ_API_KEY:
                print("  ❌ Clé API Groq manquante dans config.py")
                return False
            try:
                from groq import Groq
                client = Groq(api_key=GROQ_API_KEY)
                # Petit test rapide
                client.chat.completions.create(
                    messages=[{"role": "user", "content": "Ping"}],
                    model=GROQ_MODEL,
                )
                print(f"  ✅ Mode Groq configuré et fonctionnel (Modèle: {GROQ_MODEL})")
                return True
            except Exception as e:
                print(f"  ❌ Erreur de connexion Groq: {e}")
                return False

        if self.use_mistral:
            if not MISTRAL_API_KEY:
                print("  ❌ Clé API Mistral manquante dans config.py")
                return False
            try:
                resp = requests.get(
                    f"{MISTRAL_API_URL.rstrip('/')}/v1/models",
                    headers={"Authorization": f"Bearer {MISTRAL_API_KEY}"},
                    timeout=10,
                )
                if resp.status_code == 200:
                    print(f"  ✅ Mode Mistral configuré et fonctionnel (Modèle: {MISTRAL_MODEL})")
                    return True
                print(f"  ❌ Mistral répond avec erreur {resp.status_code}")
                return False
            except Exception as e:
                print(f"  ❌ Erreur de connexion Mistral: {e}")
                return False

        if self.use_ollama:
            try:
                # Vérification simple : lister les modèles ou juste voir si le serveur répond
                resp = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2) # Timeout court pour le check
                if resp.status_code == 200:
                    data = resp.json()
                    models = [m['name'] for m in data.get('models', [])]
                    print(f"  ✅ Serveur Ollama détecté ({OLLAMA_URL})")
                    
                    # Vérifier si le modèle existe (approximativement, car tag 'mistral:latest' vs 'mistral')
                    model_found = any(OLLAMA_MODEL in m for m in models)
                    if not model_found:
                         print(f"  ⚠️ ATTENTION : Le modèle '{OLLAMA_MODEL}' semble absent.")
                         print(f"     Modèles trouvés : {models}")
                         print(f"     Lancement du téléchargement automatique possible si configuré, sinon exécutez 'ollama pull {OLLAMA_MODEL}'")
                         # On retourne True quand même car Ollama peut puller à la volée, mais l'avertissement est utile
                    else:
                        print(f"  ✅ Modèle '{OLLAMA_MODEL}' trouvé.")
                        
                    return True
                else:
                    print(f"  ❌ Serveur Ollama répond avec erreur {resp.status_code}")
                    return False
            except requests.exceptions.ConnectionError:
                print(f"  ❌ Impossible de se connecter à Ollama sur {OLLAMA_URL}")
                return False
            except Exception as e:
                print(f"  ❌ Erreur inattendue lors du check Ollama : {e}")
                return False
        else:
            # Vérification OpenAI (juste présence clé)
            if not OPENAI_API_KEY:
                print("  ❌ Clé API OpenAI manquante dans config.py")
                return False
            print("  ✅ Mode OpenAI configuré (vérification de clé basique)")
            return True

        
    def extract_relations(self, text: str, scientist_name: str, links=None) -> dict:
        """
        Extrait les relations d'influence depuis un texte Wikipedia.
        Retourne un dictionnaire {'inspirations': [], 'inspired': []}
        """
        links = links or []
        links_hint = ", ".join(links[:200])
        # Le prompt est crucial pour obtenir du JSON propre
        prompt = f"""You are an expert analyst in the history of science.
Analyze the text below regarding "{scientist_name}" to ALGORITHMICALLY extract their influence network.

Task:
1. "inspirations": Who influenced {scientist_name}? (Mentors, predecessors, cited idols)
2. "inspired": Who did {scientist_name} influence? (Famous students, successors, admirers cited)

CRITICAL Constraints:
- Respond ONLY with valid JSON.
- DO NOT cite "{scientist_name}" themselves.
- If the text mentions no one, return empty lists.
- **HINT**: The following entities are explicitly linked in the text. Prefer using names from this list if relevant (helps with spelling):
  [{links_hint}]
- Exact expected format:
{{
  "inspirations": ["Name1", "Name2"],
  "inspired": ["Name3", "Name4"]
}}

Text to analyze:
{text[:25000]}""" # On garde une marge, Groq gère bien le grand contexte
        
        print(f"  🤖 Interrogation du LLM pour {scientist_name}...")
        
        # Logique de Fallback (Cascade)
        result = None
        
        # 1. Essai prioritaire : Groq (Rapide)
        if self.use_groq:
            result = self._call_groq(prompt)

        # 2. Fallback Mistral
        if result is None and self.use_mistral:
            result = self._call_mistral(prompt)
            
        # 3. Si Groq/Mistral ont échoué (None) ou ne sont pas activés, et qu'Ollama est dispo
        if result is None:
            if self.use_groq or self.use_mistral:
                print("  ⚠️ Échec LLM primaire -> Basculement automatique sur OLLAMA 🦙")
            
            # Tente Ollama même si USE_OLLAMA=False, car c'est un fallback explicite
            result = self._call_ollama(prompt)
        
        # 4. Dernier recours : OpenAI
        if result is None and not self.use_groq and not self.use_ollama and not self.use_mistral:
             result = self._call_openai(prompt)
             
        # Si tout a échoué ou retour None
        if result is None:
            return {"inspirations": [], "inspired": []}
            
        return result
            
    def _call_groq(self, prompt: str) -> dict:
        """Appel à l'API Groq (Ultra Rapide)."""
        try:
            from groq import Groq
            client = Groq(api_key=GROQ_API_KEY)
            
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that outputs only valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=GROQ_MODEL,
                temperature=0.1,
                response_format={"type": "json_object"}, # Force le mode JSON
            )
            
            return self._parse_json_response(chat_completion.choices[0].message.content)
            
        except Exception as e:
            print(f"  ⚠️ Erreur Groq (Rate Limit ou autre): {e}")
            return None # Renvoie None pour déclencher le fallback Ollama

    def _call_mistral(self, prompt: str) -> dict:
        """Appel à l'API Mistral."""
        if not MISTRAL_API_KEY:
            print("  ⚠️ Clé API Mistral manquante dans config.py")
            return None

        try:
            response = requests.post(
                f"{MISTRAL_API_URL.rstrip('/')}/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {MISTRAL_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": MISTRAL_MODEL,
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant that outputs only valid JSON."},
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.1,
                    "stream": False,
                },
                timeout=120,
            )
            if response.status_code != 200:
                print(f"  ⚠️ Erreur Mistral: Code {response.status_code}")
                return None
            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            return self._parse_json_response(content)
        except Exception as e:
            print(f"  ⚠️ Exception Mistral: {e}")
            return None
    
    def _call_ollama(self, prompt: str) -> dict:
        """Appel à Ollama (gratuit, local)."""
        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1  # Faible température pour plus de déterminisme
                    }
                },
                timeout=60 # Timeout généreux pour les modèles locaux
            )
            
            if response.status_code != 200:
                print(f"  ⚠️ Erreur Ollama: Code {response.status_code}")
                return {"inspirations": [], "inspired": []}
                
            result = response.json()
            return self._parse_json_response(result.get('response', '{}'))
            
        except requests.exceptions.ConnectionError:
            print("  ⚠️ Erreur de connexion à Ollama. Vérifiez qu'Ollama tourne (ollama serve).")
            return {"inspirations": [], "inspired": []}
        except Exception as e:
            print(f"  ⚠️ Exception Ollama: {e}")
            return {"inspirations": [], "inspired": []}
    
    def _call_openai(self, prompt: str) -> dict:
        """Appel à l'API OpenAI."""
        if not OPENAI_API_KEY:
            print("  ⚠️ Clé API OpenAI manquante dans config.py")
            return {"inspirations": [], "inspired": []}
            
        import openai
        openai.api_key = OPENAI_API_KEY
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1
            )
            return self._parse_json_response(response.choices[0].message.content)
        except Exception as e:
            print(f"  ⚠️ Erreur OpenAI: {e}")
            return {"inspirations": [], "inspired": []}
    
    def _parse_json_response(self, response: str) -> dict:
        """Parse la réponse JSON du LLM de manière robuste."""
        try:
            # Nettoyage basique : chercher le premier { et le dernier }
            # Cela enlève le texte introductif ou les blocs ```json
            start = response.find('{')
            end = response.rfind('}') + 1
            
            if start != -1 and end > start:
                json_str = response[start:end]
                return json.loads(json_str)
            else:
                print(f"  ⚠️ Pas de JSON trouvé dans la réponse: {response[:50]}...")
                
        except json.JSONDecodeError as e:
            print(f"  ⚠️ Erreur de décodage JSON: {e}")
            
        return {"inspirations": [], "inspired": []}
