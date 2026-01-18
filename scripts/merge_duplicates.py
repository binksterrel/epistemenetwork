import networkx as nx
import os
import shutil

# Mapping of Duplicate -> Target (Canonical Name)
MERGE_MAPPING = {
    # Henri Victor Regnault vs Henri Victor Régnault
    "Henri Victor Regnault": "Henri Victor Régnault",
    
    # Gustave Le Bon vs Gustave le Bon
    "Gustave le Bon": "Gustave Le Bon",
    
    # René Descartes vs Rene Descartes
    "Rene Descartes": "René Descartes",
    
    # Theodore von Kármán vs Theodore Von Karman
    "Theodore Von Karman": "Theodore von Kármán",
    
    # Gábor Szegő vs Gabor Szegő
    "Gabor Szegő": "Gábor Szegő"
}

def merge_nodes(graph, source, target):
    """
    Merges source node INTO target node.
    - Moves edges from source to target.
    - Preserves attributes of target (or fills from source if empty).
    - Removes source.
    """
    if source not in graph or target not in graph:
        print(f"  Skipping merge: {source} or {target} not in graph.")
        return False
    
    print(f"  Merging '{source}' -> '{target}'")
    
    # 1. Move outgoing edges (Source -> X) to (Target -> X)
    for neighbor in graph.successors(source):
        # Avoid self-loops if target is already connected
        if neighbor != target:
            # Check if edge already exists
            if not graph.has_edge(target, neighbor):
                # Copy edge data
                data = graph.get_edge_data(source, neighbor)
                graph.add_edge(target, neighbor, **data)
    
    # 2. Move incoming edges (X -> Source) to (X -> Target)
    for predecessor in graph.predecessors(source):
        if predecessor != target:
            if not graph.has_edge(predecessor, target):
                data = graph.get_edge_data(predecessor, source)
                graph.add_edge(predecessor, target, **data)
                
    # 3. Merge Node Attributes (Optional: specific rules? )
    # For now, we assume Target is the "correct" one so its attributes prevail.
    # We could fill missing attributes in Target from Source if needed.
    target_data = graph.nodes[target]
    source_data = graph.nodes[source]
    
    for k, v in source_data.items():
        if k not in target_data or not target_data[k]:
            target_data[k] = v
            
    # 4. Remove Source
    graph.remove_node(source)
    return True

def clean_none_attributes(graph):
    """NetworkX GEXF writer doesn't like None values."""
    for node, data in graph.nodes(data=True):
        for key, value in data.items():
            if value is None:
                if key == 'birth_year':
                    data[key] = 0
                else:
                    data[key] = ""

def process_file(filepath):
    print(f"Processing {filepath}...")
    try:
        if not os.path.exists(filepath):
            print(f"  File not found: {filepath}")
            return None
            
        graph = nx.read_gexf(filepath)
        initial_count = graph.number_of_nodes()
        
        merged_count = 0
        for bad_name, good_name in MERGE_MAPPING.items():
            # Check if both exist
            if bad_name in graph and good_name in graph:
                merge_nodes(graph, bad_name, good_name)
                merged_count += 1
            elif bad_name in graph and good_name not in graph:
                # Rename if only bad exists
                print(f"  Renaming '{bad_name}' -> '{good_name}'")
                mapping = {bad_name: good_name}
                nx.relabel_nodes(graph, mapping, copy=False)
                merged_count += 1
                
        if merged_count > 0:
            print(f"  Merged/Renamed {merged_count} cases.")
            print(f"  Nodes: {initial_count} -> {graph.number_of_nodes()}")
            
            clean_none_attributes(graph)
            nx.write_gexf(graph, filepath)
            print(f"  Saved updated graph to {filepath}")
            return filepath
        else:
            print("  No changes needed.")
            return None
            
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")
        return None

if __name__ == "__main__":
    # Files to process
    files_to_check = [
        "output/scientist_graph_merged.gexf",
        "output/scientist_graph_enriched.gexf",
        "output/scientist_graph_clean.gexf",
        "output/scientist_graph.gexf"
    ]
    
    for f in files_to_check:
        processed_file = process_file(f)
        
        # If successfully processed and modified, copy to saves/version5
        if processed_file:
            target_dir = "saves/version5"
            if os.path.exists(target_dir):
                basename = os.path.basename(processed_file)
                destination = os.path.join(target_dir, basename)
                shutil.copy2(processed_file, destination)
                print(f"  Copied to {destination}")
            else:
                print(f"  Warning: Target directory {target_dir} does not exist.")
        
        print("-" * 50)
