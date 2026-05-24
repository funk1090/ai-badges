# Gold Assignment 2 — Python Client for Ollama

This module contains a minimal and clean Python client for interacting with **Ollama**, a local LLM runtime that allows you to run models such as LLaMA, Mistral, Phi, Gemma, and others directly on your machine.

---

## 📌 Purpose

The goal of this assignment is to:
- Understand how to interact programmatically with a local LLM
- Send prompts and receive responses using Python
- Build a reusable client that can be integrated into larger pipelines
- Explore local inference without relying on cloud APIs

---

## 📂 Contents

- `ollama_client.py` — Python wrapper for sending prompts to an Ollama model  
- `README.md` — Documentation for setup and usage  

---

## ⚙️ Requirements

To run this module, you need:

### **1. Ollama installed locally**
Download from:  
https://ollama.com/download

### **2. At least one model pulled**
Example:

ollama pull llama3


or

ollama pull mistral


### **3. Python dependencies**
(Handled by your main `requirements.txt`)

---

## 🚀 How to Run

### **Run the client script**

python ollama_client.py


Inside the script, you can customize:
- The model name  
- The prompt  
- The temperature  
- The max tokens  

---

## 🧠 Example Usage (inside the script)

```python
from ollama_client import OllamaClient

client = OllamaClient(model="llama3")
response = client.ask("Explain transfer learning in simple terms.")
print(response)

📝 Notes
This module is intentionally simple and modular

It can be extended to support streaming, embeddings, or chat history

Works offline once models are downloaded

Ideal for integrating into RAG or agent pipelines

🔧 Next Steps (optional)
Add support for embeddings

Add a streaming response mode

Integrate with FAISS or GPT4ALL

Build a CLI wrapper