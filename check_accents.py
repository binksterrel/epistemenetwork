import xml.etree.ElementTree as ET
import unicodedata
import os
import sys

def normalize_text(text):
    if not text:
        return ""
    # Normalize unicode characters to decompose combined characters (like é -> e + ')
    # then filter out non-spacing mark characters (accents)
    normalized = unicodedata.normalize('NFKD', text)
    result = "".join([c for c in normalized if not unicodedata.category(c).startswith('M')])
    return result.lower().strip()

def check_file(filepath):
    print(f"Checking {filepath}...")
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return

    # Namespace handling might be needed for GEXF
    # GEXF usually looks like {http://www.gexf.net/1.2draft}gexf
    # But ElementTree default finding with tags often ignores namespaces if not strict or using *
    
    # Let's find all nodes. The tag is usually {namespace}node
    # We can iterate everything and check if tag ends with 'node'
    
    nodes_by_norm = {}
    
    count = 0
    namespace = ""
    # Extract namespace if present
    if root.tag.startswith("{"):
        namespace = root.tag.split("}")[0] + "}"
        
    # Find nodes
    # If namespace exists, use it
    nodes = root.findall(f".//{namespace}node")
    if not nodes:
        # Fallback to searching all elements if namespace is tricky
        nodes = [elem for elem in root.iter() if "node" in elem.tag and elem.tag.endswith("node")]

    print(f"Found {len(nodes)} nodes.")

    for node in nodes:
        label = node.get('label')
        node_id = node.get('id')
        
        if not label:
            label = node_id # Fallback to ID if label is missing
            
        if not label:
            continue
            
        norm = normalize_text(label)
        
        if norm not in nodes_by_norm:
            nodes_by_norm[norm] = []
        
        nodes_by_norm[norm].append({'label': label, 'id': node_id})
        count += 1

    duplicates_found = False
    print("\n--- Potential Duplicates (Accent/Case variations) ---\n")
    
    for norm, instances in nodes_by_norm.items():
        if len(instances) > 1:
            # Check if they are actually different strings (ignoring exact identical duplicates for now, 
            # unless user wants to know about exact duplicates too? User specifically asked for accent diffs)
            
            unique_labels = set(inst['label'] for inst in instances)
            
            if len(unique_labels) > 1:
                duplicates_found = True
                print(f"Key: '{norm}'")
                for inst in instances:
                    print(f"  - Label: '{inst['label']}' (ID: {inst['id']})")
                print("")

    if not duplicates_found:
        print("No accent/case duplicates found among different labels.")

if __name__ == "__main__":
    # Check the likely files
    files_to_check = [
        "output/scientist_graph_merged.gexf",
        "output/scientist_graph_enriched.gexf",
        "output/scientist_graph_clean.gexf",
        "output/scientist_graph.gexf"
    ]
    
    found = False
    for f in files_to_check:
        if os.path.exists(f):
            check_file(f)
            found = True
            print("-" * 50)
            
    if not found:
        print("No GEXF files found in output/")
