from graph_builder import GraphBuilder
from graph_analyzer import GraphAnalyzer
from visualizer import GraphVisualizer
from config import START_SCIENTIST
import os
import sys

def main():
    print("="*60)
    print("🔬 PROJET GRAPHE D'INFLUENCE SCIENTIFIQUE")
    print("="*60)
    
    # 0. Préparation
    os.makedirs("output", exist_ok=True)
    
    # Vérification Health Check LLM
    llm_check = GraphBuilder().llm 
    # Note: GraphBuilder instancie LLMExtractor, mais on peut aussi l'instancier directement
    # Pour faire propre, importons LLMExtractor ici ou utilisons celui du builder
    from llm_extractor import LLMExtractor
    if not LLMExtractor().check_connection():
        print("\n" + "="*60)
        print("🛑 ERREUR CRITIQUE : LLM INTROUVABLE")
        print("="*60)
        print("Le programme ne peut pas fonctionner sans accès à une IA.")
        if START_SCIENTIST == "Albert Einstein": # Exemple
             print("👉 Si vous utilisez Ollama (défaut) : Assurez-vous d'avoir installé et lancé Ollama.")
             print("   Téléchargement : https://ollama.com")
             print("   Lancement : Commande 'ollama serve' dans un terminal.")
             print("👉 Si vous utilisez OpenAI : Vérifiez votre clé API dans config.py.")
        print("="*60 + "\n")
        return
    
    # 1. Construction
    builder = GraphBuilder()
    try:
        graph = builder.build_influence_graph(START_SCIENTIST)
    except KeyboardInterrupt:
        print("\n🛑 Interruption utilisateur. Sauvegarde partielle...")
        graph = builder.graph
    except Exception as e:
        print(f"\n❌ Erreur critique: {e}")
        return

    if graph.number_of_nodes() == 0:
        print("❌ Aucun nœud récupéré. Vérifiez votre connexion internet ou la configuration.")
        return

    # 2. Export données brutes
    builder.save_graph("output/scientist_graph.gexf")
    
    # 3. Analyse
    analyzer = GraphAnalyzer(graph)
    analyzer.analyze()
    
    # 4. Visualisation
    visualizer = GraphVisualizer(graph)
    visualizer.create_interactive_html("output/index.html")
    
    print("\n✅ Terminé avec succès!")

if __name__ == "__main__":
    # Vérification des dépendances au lancement
    try:
        import wikipediaapi
        import networkx
        import pyvis
    except ImportError as e:
        print(f"❌ Dépendance manquante: {e}")
        print("   Exécutez: pip install -r requirements.txt")
        sys.exit(1)
        
    main()
