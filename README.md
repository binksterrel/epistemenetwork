# 🔬 RÉSEAU D'INFLUENCE SCIENTIFIQUE (V5)

Un outil interactif complet pour **générer, nettoyer, enrichir et visualiser** les connexions entre scientifiques à travers l'histoire, propulsé par l'IA (LLM).

![Aperçu du Graphe](output/preview.png)

## 📊 Statistiques Actuelles (Version 5 - Final)
Le graphe a été généré, nettoyé et consolidé pour offrir une vue précise de l'histoire des sciences.

| Métrique | Valeur |
|----------|--------|
| **Nœuds** | **~1 726** scientifiques |
| **Arêtes** | **~2 520** relations d'influence |
| **Période** | **1105 - 2006** (XIIe - XXIe siècle) |
| **Qualité** | **100% Connecté** (Pas de nœuds isolés, nettoyage "Giant Component") |
| **Donnée** | **Enrichie** (Domaines scientifiques identifiés par IA) |

---

## 🚀 Installation & Démarrage

### 1. Pré-requis
*   Python 3.9+
*   Une clé API (Groq, OpenAI, Mistral) **OU** Ollama installé localement.

### 2. Installation
```bash
# Cloner le projet
git clone https://github.com/binksterrel/GraphReseauScientifique.git
cd GraphReseauScientifique

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # Sur Mac/Linux
# .venv\Scripts\activate # Sur Windows

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Configuration
Ouvrez `config.py` et configurez votre LLM :
```python
USE_GROQ = True  # Recommandé pour la vitesse
GROQ_API_KEY = "votre_cle_ici"

# OU pour une utilisation locale gratuite :
USE_OLLAMA = True
```

---

## 🛠️ Workflow Complet (Pipeline)

Le projet suit un pipeline strict pour garantir la qualité des données.

### Étape 1 : Génération du Graphe
Scrape Wikipédia et utilise le LLM pour extraire les relations "Inspired by".
```bash
python3 main.py
```

### Étape 2 : Nettoyage Expert (Post-Processing)
Standardisation des noms, fusion des doublons (ex: Oppenheimer), suppression du "bruit" et des isolés.
```bash
python3 post_process_graph.py
```

### Étape 3 : Enrichissement des Données (Champs)
Interroge l'IA pour identifier le domaine scientifique (Physics, Chemistry...) des profils manquants.
```bash
python3 enrich_fields.py
```

### Étape 4 : Visualisation & Rapports
Génère le site web statique (`index.html`) et les rapports texte.
```bash
python3 visualize_current.py
python3 export_text_report.py
```

> **Note :** Pour lancer le serveur web localement :
> `python3 -m http.server 8000 --directory output`

---

## 📂 Structure du Fichier

### 🔹 Scripts Cœur (Core)
*   `main.py` : Orchestrateur de la génération.
*   `post_process_graph.py` : Algorithmes de nettoyage et fusion (NetworkX).
*   `enrich_fields.py` : Script d'enrichissement de métadonnées.
*   `llm_extractor.py` : Interface unifiée pour tous les LLMs.
*   `config.py` : Paramètres globaux.

### 🔹 Dossiers
*   `output/` : Contient le site web généré (`index.html`, `graph.html`) et le fichier GEXF.
*   `saves/` : Backups des versions majeures (V1, V2, ... V5).
*   `scripts/archive/` : Anciens scripts utilitaires (nettoyage, audit).

---

## 🌟 Fonctionnalités du Site Web

*   **Graphe interactif** (Zoom, Pan, Physics engine).
*   **Recherche temps réel** de scientifiques.
*   **Filtres temporels** (Curseur d'années).
*   **Coloration dynamique** par communauté ou domaine.
*   **Fiches détaillées** au clic (Wikipedia summary).

---

## 📝 Licence & Auteur
**Auteur** : Terrel Nuentsa
**Université** : L3 MIASHS - Graphes et Open Data
Projet Universitaire - Semestre 2
mtn