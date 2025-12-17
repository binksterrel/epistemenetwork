import networkx as nx

class GraphAnalyzer:
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        
    def analyze(self) -> dict:
        """
        Calcule et affiche les métriques de centralité.
        """
        if self.graph.number_of_nodes() == 0:
            print("⚠️ Le graphe est vide, impossible d'analyser.")
            return {}

        print("\n📊 ANALYSE DU RÉSEAU")
        print("=" * 50)
        
        results = {}
        
        # 1. Degree Centrality (Le plus connecté globalement)
        try:
            degree = nx.degree_centrality(self.graph)
            results['degree'] = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:10]
            
            print("\n🔗 TOP 10 - Centralité de Degré (Hubs):")
            for name, score in results['degree']:
                print(f"   {name:<25} : {score:.4f}")
        except:
            print("   (Erreur calul degree)")
        
        # 2. PageRank (Influence recursive - l'algo de Google)
        try:
            pagerank = nx.pagerank(self.graph)
            results['pagerank'] = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]
            
            print("\n⭐ TOP 10 - PageRank (Influence réelle):")
            for name, score in results['pagerank']:
                print(f"   {name:<25} : {score:.4f}")
        except:
            print("   (Impossible de calculer PageRank sur ce graphe)")
        
        # 3. Betweenness (Les ponts entre communautés)
        try:
            betweenness = nx.betweenness_centrality(self.graph)
            results['betweenness'] = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]
            
            print("\n🌉 TOP 10 - Intermédiarité (Passeurs de savoir):")
            for name, score in results['betweenness']:
                print(f"   {name:<25} : {score:.4f}")
        except:
            print("   (Erreur calcul betweenness)")

        return results
