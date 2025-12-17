import networkx as nx
from collections import deque
import time
from wikipedia_client import WikipediaClient
from llm_extractor import LLMExtractor
from config import MAX_DEPTH, MAX_SCIENTISTS

class GraphBuilder:
    def __init__(self):
        self.graph = nx.DiGraph()  # Graphe orienté
        self.wiki_client = WikipediaClient()
        self.llm = LLMExtractor()
        self.visited = set()
        
    def build_influence_graph(self, start_scientist: str) -> nx.DiGraph:
        """
        Construit le graphe d'influence en utilisant un parcours BFS (Largeur d'abord).
        """
        # File d'attente contenant: (nom_scientifique, profondeur_actuelle)
        queue = deque([(start_scientist, 0)])
        
        print(f"\n🚀 DÉMARRAGE de la construction du graphe depuis: {start_scientist}")
        print(f"   Max Profondeur: {MAX_DEPTH} | Max Scientifiques: {MAX_SCIENTISTS}")
        print("-" * 60)
        
        while queue and len(self.visited) < MAX_SCIENTISTS:
            current_scientist, depth = queue.popleft()
            
            # 1. Vérifications préliminaires
            if current_scientist in self.visited:
                continue
            if depth > MAX_DEPTH:
                continue
                
            print(f"🔎 [{len(self.visited)+1}/{MAX_SCIENTISTS}] Analyse de: {current_scientist} (Prof: {depth})")
            
            # 2. Récupération du texte
            wiki_text = self.wiki_client.get_scientist_text(current_scientist)
            
            if not wiki_text:
                print(f"  ❌ Pas de page Wikipedia trouvée. Ignore.")
                continue
            
            # 3. Ajout au graphe et marquage comme visité
            self.visited.add(current_scientist)
            self.graph.add_node(current_scientist, depth=depth)
            
            # Si on atteint la profondeur max, on ne cherche pas les voisins
            # (on l'ajoute juste comme feuille)
            if depth == MAX_DEPTH:
                print(f"  🛑 Profondeur max atteinte, pas d'analyse des relations.")
                continue
                
            # 4. Extraction des relations via LLM
            relations = self.llm.extract_relations(wiki_text, current_scientist)
            
            # 5. Traitement des "inspirations" (A a inspiré current)
            # Arc: A -> current
            inspirations = relations.get('inspirations', [])
            for person in inspirations:
                if person == current_scientist:
                    continue # Pas d'auto-inspiration
                if self._is_valid_name(person):
                    # Ajouter l'arc
                    self.graph.add_edge(person, current_scientist, relation="inspired")
                    # Ajouter à la file
                    if person not in self.visited:
                        queue.append((person, depth + 1))
            
            # 6. Traitement des "inspirés" (current a inspiré B)
            # Arc: current -> B
            inspired_list = relations.get('inspired', [])
            for person in inspired_list:
                if person == current_scientist:
                    continue
                if self._is_valid_name(person):
                    # Ajouter l'arc
                    self.graph.add_edge(current_scientist, person, relation="inspired")
                    # Ajouter à la file
                    if person not in self.visited:
                        queue.append((person, depth + 1))
            
            print(f"  ✅ Relations trouvées: {len(inspirations)} inspirations, {len(inspired_list)} inspirés.")
            
            # Petite pause pour être poli envers les APIs
            time.sleep(0.5)
        
        print("-" * 60)
        print(f"🏁 CONSTRUCTION TERMINÉE")
        print(f"   Total Nœuds: {self.graph.number_of_nodes()}")
        print(f"   Total Arêtes: {self.graph.number_of_edges()}")
        
        return self.graph
    
    def _is_valid_name(self, name: str) -> bool:
        """Filtre basique pour éviter les erreurs du LLM."""
        if not name or not isinstance(name, str):
            return False
        # Doit faire au moins 3 caractères et contenir un espace (Prénom Nom)
        if len(name) < 3 or ' ' not in name:
            return False
        return True
    
    def save_graph(self, filename: str = "output/scientist_graph.gexf"):
        """Exporte le graphe pour Gephi."""
        try:
            nx.write_gexf(self.graph, filename)
            print(f"💾 Graphe exporté vers: {filename}")
        except Exception as e:
            print(f"⚠️ Erreur lors de l'export: {e}")
