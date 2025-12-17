# Configuration du projet Graphe d'Influence Scientifique

# ============================================================
# CONFIGURATION LLM
# ============================================================

# Clé API OpenAI (laisser vide si vous utilisez Ollama)
OPENAI_API_KEY = ""

# True = utiliser Ollama (gratuit, local)
# False = utiliser OpenAI (payant, nécessite clé API)
# False = utiliser OpenAI (payant, nécessite clé API)
USE_OLLAMA = False

# Configuration Groq (API Rapide)
USE_GROQ = True
GROQ_API_KEY = "TO_BE_DEFINED"
GROQ_MODEL = "llama-3.3-70b-versatile"

# Configuration Ollama
OLLAMA_URL = "http://127.0.0.1:11434"
OLLAMA_MODEL = "mistral"  # ou "llama2", "codellama", etc.

# ============================================================
# PARAMÈTRES DE L'ALGORITHME
# ============================================================

# Profondeur maximale de récursion (3-4 recommandé)
# Profondeur maximale de récursion (3-4 recommandé)
MAX_DEPTH = 6

# Nombre maximum de scientifiques à analyser
MAX_SCIENTISTS = 250

# Scientifique de départ
START_SCIENTIST = "Albert Einstein"

# Langue Wikipedia ('fr' pour français, 'en' pour anglais)
WIKIPEDIA_LANGUAGE = "en"
