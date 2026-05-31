from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
embeddings = None

def add_document(text, metadata=None):
    global embeddings
    emb = model.encode([text]).astype("float32")
    documents.append({"text": text, "metadata": metadata})

    if embeddings is None:
        embeddings = emb
    else:
        embeddings = np.vstack([embeddings, emb])

def query(text, n_results=3):
    global embeddings
    if embeddings is None:
        return []

    q_emb = model.encode([text]).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    distances, indices = index.search(q_emb, n_results)

    return [documents[i] for i in indices[0]]
