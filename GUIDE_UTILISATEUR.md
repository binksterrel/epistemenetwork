# 📘 Guide Utilisateur de l'Interface

Une fois le fichier `output/index.html` ouvert dans votre navigateur (Chrome, Firefox, Safari), voici comment utiliser l'interface interactive.

## 1. 🔍 Exploration du Graphe

*   **Navigation** :
    *   **Zoom** : Utilisez la molette de la souris.
    *   **Déplacement** : Cliquez et glissez dans le vide pour bouger la caméra.
    *   **Sélection** : Cliquez sur un nœud (rond) pour le mettre en surbrillance et voir ses connexions directes.

*   **Légende (Couleurs)** :
    *   Les nœuds sont colorés par **Communauté** (groupes de scientifiques interconnectés).
    *   Regardez la légende flottante en bas à droite pour voir le nom du "Leader" de chaque cercle (ex: *Cercle de Henri Poincaré*).

*   **Taille des Nœuds** :
    *   Plus un rond est **gros**, plus ce scientifique est influent (calculé par *PageRank*).

## 2. 📝 Panneau Latéral (Information)

Cliquez sur un scientifique pour ouvrir le panneau de droite :
*   **Résumé** : Biographie courte extraite de Wikipédia.
*   **Indice d'Influence** : Un score montrant son importance dans ce réseau spécifique.
*   **Lien Wikipédia** : Ouvre sa page officielle dans un nouvel onglet.
*   **Supprimer** : Retire ce nœud du graphe (pour nettoyer les erreurs).

## 3. 🔦 Fonctionnalités Avancées (Barre du haut)

### Recherche Rapide
*   Tapez quelques lettres dans la barre de recherche (en haut à gauche).
*   Cliquez sur le nom proposé : la caméra zoomera directement sur lui.

### Chemin le plus court (Pathfinding)
Voulez-vous savoir comment **Aristote** est relié à **Einstein** ?
1.  Cliquez sur le bouton **"Chemin"** (icône de route 🔀).
2.  Sélectionnez le scientifique de **Départ**.
3.  Sélectionnez le scientifique d'**Arrivée**.
4.  Cliquez sur **"Trouver le chemin"**.
5.  👀 **Observez !** Une ligne pointillée animée (style "fourmis") va tracer la route connectant les deux personnes.

### Clic sur les Liens (Flèches)
*   Cliquez sur une flèche grise entre deux personnes.
*   Une notification apparaîtra pour préciser la relation : *"Albert Einstein A INFLUENCÉ Satyendra Nath Bose"*.

## 4. ⚙️ Contrôles Techniques (Bas à gauche)

*   **Physique** : Activez/Désactivez le mouvement des bulles. (Utile si ça bouge trop).
*   **Réinitialiser la Vue** : Recentre la caméra si vous êtes perdu.
