# Gold Assignment 3 — RAG with GPT4ALL + FAISS

This module implements a complete **Retrieval‑Augmented Generation (RAG)** pipeline using:

- **GPT4ALL** as a local LLM  
- **FAISS** as a vector store  
- **SentenceTransformers** for embeddings  
- **Python** for orchestration  

The goal is to build a fully local RAG system capable of indexing documents, retrieving relevant chunks, and generating context‑aware responses.

---

## 📂 Contents

- `rag_gpt4all.ipynb` — Full notebook with explanations and step‑by‑step execution  
- `rag_gpt4all.py` — Script version of the RAG pipeline  
- `data/` — Folder for raw text documents to index (not included in the repo)  

---

## 🧠 Features

- Document loading and preprocessing  
- Text chunking with configurable size and overlap  
- Embedding generation using SentenceTransformers  
- FAISS index creation and similarity search  
- Local inference using GPT4ALL models (`.gguf`)  
- RAG pipeline combining retrieval + generation  

---

## ⚙️ Requirements

### **1. GPT4ALL installed**
Download from:  
https://gpt4all.io

Or install via pip:

pip install gpt4all


### **2. A `.gguf` model downloaded**
Examples:

- `mistral-7b-instruct.gguf`
- `llama3-8b-instruct.gguf`
- `phi-3-mini.gguf`

Place the model in your GPT4ALL models directory.

### **3. Python dependencies**
Handled by your main `requirements.txt`.

---

## 🚀 How to Run

### **Run the script**

python rag_gpt4all.py


### **Run the notebook**
Open `rag_gpt4all.ipynb` in:

- VS Code  
- Jupyter  
- Google Colab (recommended for GPU embeddings)  

---

## 📁 Dataset Structure

Place your documents inside:

data/
├── doc1.txt
├── doc2.txt
└── ...


The pipeline will automatically:

- Load all `.txt` files  
- Chunk them  
- Embed them  
- Build a FAISS index  

---

## 🧪 Example Query (inside the script)

```python
from rag_gpt4all import RAGPipeline

rag = RAGPipeline()
response = rag.ask("Explain the main ideas of document 1.")
print(response)

📝 Notes
Models are not included in the repository

FAISS indexes are generated locally and ignored by .gitignore

This module is fully offline once models and embeddings are available

Ideal foundation for agent‑based systems or advanced RAG architectures

🔧 Possible Extensions
Add metadata filtering

Add support for PDFs

Add streaming responses

Replace FAISS with ChromaDB

Integrate with AutoGen agents