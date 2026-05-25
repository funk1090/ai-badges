import os
import faiss
import numpy as np
from gpt4all import GPT4All
from sentence_transformers import SentenceTransformer

class RAGPipeline:
    def __init__(self, model_name="gpt4all-falcon-newbpe-q4_0.gguf", embed_model="all-MiniLM-L6-v2"):
        # Force CPU for embeddings
        self.embedder = SentenceTransformer(embed_model, device="cpu")
        # GPT4All will choose CPU/GPU depending on its own runtime; it's fine to leave default
        self.llm = GPT4All(model_name)
        self.index = None
        self.documents = []
        self.index_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vector_store.faiss")

    def load_documents(self, folder="documents"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Documents folder not found: {folder_path}")
        docs = []
        for file in sorted(os.listdir(folder_path)):
            if file.endswith(".txt"):
                with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                    docs.append(f.read())
        self.documents = docs
        return docs

    def build_index(self):
        if not self.documents:
            raise ValueError("No documents loaded.")
        # Compute embeddings on CPU
        embeddings = self.embedder.encode(self.documents, show_progress_bar=True, convert_to_numpy=True)
        dim = embeddings.shape[1]

        # Create FAISS index and add embeddings
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings).astype('float32'))

        # Save index for faster reuse
        faiss.write_index(self.index, self.index_path)

    def load_index(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            return True
        return False

    def retrieve(self, query, k=2):
        if self.index is None:
            raise RuntimeError("Index not built or loaded.")
        query_emb = self.embedder.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(np.array(query_emb).astype('float32'), k)
        return [self.documents[i] for i in indices[0] if i != -1]
        
    def generate_answer(self, query):
        context_docs = self.retrieve(query)
        # debug: show which docs were retrieved
        print("DEBUG: Retrieved documents:")
        for i, d in enumerate(context_docs):
            snippet = d[:120].replace("\n", " ")
            print(f"--- Doc {i+1} (first 120 chars): {snippet}")

        context = "\n\n".join(context_docs)

        prompt = f"""You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""
        # GPT4All generate returns a string or generator depending on version; handle accordingly
        out = self.llm.generate(prompt)
        # If generate returns an object, convert to string
        if isinstance(out, (list, tuple)):
            return "\n".join(map(str, out))
        return str(out)

if __name__ == "__main__":
    rag = RAGPipeline()

    print("Loading documents...")
    rag.load_documents()

    # Try to load existing index, otherwise build it
    if rag.load_index():
        print("Loaded existing FAISS index.")
    else:
        print("Building FAISS index (this may take a moment)...")
        rag.build_index()
        print("Index built and saved.")

    print("Ready. Ask something (type 'exit' to quit):")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        try:
            answer = rag.generate_answer(q)
            print("Model:", answer)
        except Exception as e:
            print("Error:", e)
