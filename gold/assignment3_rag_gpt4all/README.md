Gold Assignment 3 — Local RAG Pipeline with GPT4All and FAISS
This assignment implements a local Retrieval‑Augmented Generation (RAG) pipeline using:

Sentence‑Transformers for dense embeddings

FAISS for vector search

GPT4All as a fully local LLM for answer generation

The goal is to demonstrate how to build an end‑to‑end RAG system that retrieves relevant information from local documents and uses it to generate grounded responses.

📂 Project Structure
gold/assignment3_rag_gpt4all/
 ├── rag_pipeline.py
 ├── documents/
 │     ├── transfer_learning.txt
 │     ├── computer_vision.txt
 │     └── ai_history.txt
 ├── vector_store.faiss
 ├── README.md
 └── requirements.txt

File descriptions

rag_pipeline.py — Main RAG pipeline (embeddings → FAISS retrieval → GPT4All generation).

documents/ — Source text files used for retrieval.

vector_store.faiss — Saved FAISS index (created automatically on first run).

requirements.txt — Python dependencies for the assignment.
⚙️ Requirements
Install dependencies:
pip install -r requirements.txt

Typical requirements.txt:
gpt4all
sentence-transformers
faiss-cpu
numpy
torch
transformers

Notes:

The first run downloads the embedding model and the GPT4All model.

The pipeline forces CPU for embeddings to avoid CUDA compatibility issues.

GPT4All will run on CPU unless a compatible GPU backend is available.

🚀 How to Run
From the root of the repository:
cd gold/assignment3_rag_gpt4all
python rag_pipeline.py
On first run:

Documents are loaded

Embeddings are computed

A FAISS index is built and saved

GPT4All loads the local model

On subsequent runs, the FAISS index loads instantly.

🧠 How the RAG Pipeline Works
Load documents from the documents/ folder

Encode documents using all-MiniLM-L6-v2

Build or load a FAISS vector index

Retrieve top‑k documents for a user query

Construct a context prompt

Generate an answer using GPT4All with the retrieved context

This ensures answers are grounded in your local documents.

💬 Example Usage
Ready. Ask something (type 'exit' to quit):

You: What is transfer learning?
Model: Transfer learning is a machine learning technique where a model trained on one task is reused...

You: What does computer vision do?
Model: Computer vision is a field of artificial intelligence focused on enabling machines to interpret...

You: When did AI research begin?
Model: Artificial intelligence research began in the 1950s with early symbolic systems...
🧪 Recommended Test Prompts
These prompts validate retrieval and grounding:

What is transfer learning?

What does computer vision do?

When did AI research begin?

Explain how you can reuse a pretrained model for a new task.

Who invented the transformer architecture. (tests out‑of‑document behavior)
📌 Notes
The pipeline runs fully offline once models are downloaded.

FAISS indexing is saved to speed up future runs.

You can extend the system with chunking, metadata, or larger document sets.

To use a different GPT4All model, change the model_name in rag_pipeline.py.