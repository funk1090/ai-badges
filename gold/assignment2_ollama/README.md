# 📘 **Gold Assignment 2 — Ollama Chat Client (Python)**

This module implements a **Python chat client** for interacting with local Large Language Models (LLMs) running through **Ollama**, such as Llama 3, Mistral, Phi, Gemma, and others.

The goal of this assignment is to demonstrate how to:

- Send prompts to a local LLM via the Ollama API  
- Maintain a conversation with message history  
- Receive responses programmatically  
- Build a reusable and extensible chat client  

---

## 📂 Project Structure

- `ollama_chat_client.py` — Chat client using the `/api/chat` endpoint  
- `README.md` — Documentation for this assignment  

---

## ⚙️ Requirements

### 1. Install Ollama  
Download from:  
[https://ollama.com/download](https://ollama.com/download)

### 2. Pull at least one model  
Example:

```
ollama pull llama3
```

### 3. Install Python dependencies  
Only `requests` is required:

```
pip install requests
```

---

## 🚀 How to Run the Chat Client

Run:

```
python ollama_chat_client.py
```

You will see:

```
Chat started. Type 'exit' to quit.

You: Hello
Model: Hello! How can I help you today?
```

You can continue chatting naturally thanks to the internal message history.

---

## 🧠 How the Client Works

The file `ollama_chat_client.py` implements:

- A wrapper around the `/api/chat` endpoint  
- Persistent conversation history  
- Support for any Ollama model  
- A simple interactive loop  

Example usage inside the script:

```python
chat = OllamaChatClient(model="llama3")
reply = chat.ask("Explain transfer learning in simple terms.")
print(reply)
```

---

## 📌 Notes

- Works fully offline once the model is downloaded  
- Ideal for local experimentation, RAG pipelines, or agent systems  
- Can be extended to support streaming, embeddings, or multi‑model routing  