# Silver Assignment 2 — AutoGen Multi‑Agent System

This module contains examples and experiments using **Microsoft AutoGen**, a framework for building multi‑agent systems where LLM‑powered agents collaborate, use tools, and solve tasks autonomously.

The goal of this assignment is to explore:
- Multi‑agent collaboration  
- Tool‑enabled reasoning  
- RAG‑enhanced agents  
- Local or cloud LLM integration  
- Autonomous task execution  

---

## 📂 Contents

- `autogen_rag_agent.py` — Example of an AutoGen agent with RAG capabilities  
- `demo.ipynb` — Notebook demonstrating agent interactions (to be added)  
- `README.md` — Documentation  

---

## 🧠 What AutoGen Enables

AutoGen allows you to build systems where multiple agents can:

- Talk to each other  
- Share intermediate reasoning  
- Use tools (Python functions, APIs, RAG pipelines)  
- Plan and execute tasks  
- Ask for clarification when needed  
- Produce structured outputs  

This assignment focuses on **practical agent design**, not just theory.

---

## ⚙️ Requirements

Install AutoGen:

pip install pyautogen


Optional (for RAG):

pip install sentence-transformers faiss-cpu gpt4all


Optional (for local LLMs):

- Ollama  
- GPT4ALL  
- LM Studio  

---

## 🚀 How to Run

### **Run the RAG‑enabled agent**

python autogen_rag_agent.py


Inside the script, you can configure:

- The LLM provider (OpenAI, Azure, local)  
- The system prompt  
- The tools available to the agent  
- The RAG pipeline (FAISS + embeddings)  

---

## 🧪 Example Agent Interaction (inside the script)

```python
from autogen_rag_agent import create_rag_agent

agent = create_rag_agent()
response = agent.run("Summarize the key ideas from the indexed documents.")
print(response)

🧩 Architecture Overview
A typical AutoGen setup includes:

Assistant Agent  
Handles reasoning, planning, and generation.

User Proxy Agent  
Simulates a user and provides instructions.

Tools  
Python functions or external APIs the agent can call.

RAG Pipeline  
Provides context retrieved from documents.

📝 Notes
AutoGen is more flexible and powerful than AutoGPT

Agents can call Python functions directly

You can integrate FAISS, GPT4ALL, or Ollama

Supports multi‑agent conversations

Works with both cloud and local models

🔧 Possible Extensions
Add multiple agents (e.g., researcher + coder)

Add a tool for web search

Add a tool for file writing

Integrate the RAG pipeline from Gold Assignment 3

Build a fully autonomous research assistant

📌 Conclusion
This assignment demonstrates how to build intelligent, tool‑enabled, multi‑agent systems using AutoGen.
It serves as a foundation for more advanced agent architectures and autonomous workflows.