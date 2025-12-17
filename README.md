# 🔬 RÉSEAU SCIENTIFIQUE Scientifique

Un outil interactif pour **générer, visualiser et analyser** les connexions entre scientifiques à partir de leurs pages Wikipédia, propulsé par l'Intelligence Artificielle.

![Aperçu du Graphe](output/preview.png)
*(Générez une capture d'écran pour remplacer cette image)*

## 🌟 Fonctionnalités

*   **Extraction automatique** : Analyse des pages Wikipédia via LLM (Groq, OpenAI ou Ollama) pour trouver qui a influencé qui.
*   **Visualisation Interactive** : Graphe dynamique avec zoom, recherche et filtres.
*   **Algorithmes de Graphe** :
    *   **PageRank** : Taille des nœuds selon leur influence globale.
    *   **Communautés** : Couleurs selon les "écoles de pensée" ou groupes historiques.
    *   **Chemin le plus court** : Trouvez le lien caché entre deux scientifiques (animation "fourmis").
*   **Documentation Riche** : Accès direct aux résumés et liens Wikipédia depuis l'interface.

## 🚀 Installation

Pré-requis : Python 3.9+

1.  **Cloner ou télécharger le dossier du projet.**
2.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

    > **Note pour Windows** 🪟 :
    > Si `python3` n'est pas reconnu, utilisez `python`.
    > Pour activer un environnement virtuel (optionnel) : `.\venv\Scripts\activate`

## ⚙️ Configuration

Ouvrez le fichier `config.py` pour ajuster les paramètres :

*   **Choix du LLM** :
    *   `USE_GROQ = True` (Recommandé pour la vitesse : 300+ tokens/s).
    *   `USE_OLLAMA = True` (Pour une exécution locale gratuite, plus lent).
    *   `USE_OPENAI = True` (GPT-3.5/4).
*   **Limites du Graphe** :
    *   `MAX_DEPTH` : Profondeur d'exploration depuis le point de départ (ex: 6).
    *   `MAX_SCIENTISTS` : Nombre maximum de nœuds (ex: 250).
*   **Point de départ** :
    *   `START_SCIENTIST = "Albert Einstein"` (Changez-le pour explorer un autre domaine !).

## 🏃‍♂️ Utilisation

1.  **Lancer la génération du graphe :**
    ```bash
    python3 main.py
    ```
    *Le script va scanner Wikipédia, interroger l'IA, et construire le graphe en temps réel.*

2.  **Ouvrir la visualisation :**
    Ouvrez simplement le fichier généré dans votre navigateur :
    `output/index.html`

## 📂 Structure du projet

*   `main.py` : Chef d'orchestre, lance le processus.
*   `wikipedia_client.py` : Gère la récupération des textes Wikipédia.
*   `llm_extractor.py` : Interface avec l'IA (Groq/Ollama) pour extraire les relations JSON.
*   `graph_analyzer.py` : Calcule PageRank, communautés et statistiques.
*   `visualizer.py` : Génère le fichier HTML/JS moderne.
*   `config.py` : Tous les réglages modifiables.

---

