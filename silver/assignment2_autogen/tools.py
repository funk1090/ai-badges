# tools.py
def search_rag(query, rag):
    results = rag.query(query)
    return results

def save_memory(memory_file, data):
    import json
    with open(memory_file, "w") as f:
        json.dump(data, f)
    return "Memory saved."
