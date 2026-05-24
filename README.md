# 🧠 AI Badges — Gold & Silver Assignments  
Author: **Enzo Juan Huanca Acevedo**

This repository contains the full implementation of the **Gold** and **Silver** badge assignments for the AI program.  
It includes notebooks, Python scripts, RAG pipelines, local LLM integrations, and autonomous agent experiments.

---

## 📂 Repository Structure

ai-badges/
├── gold/
│   ├── assignment1_resnet/          # Fine‑tuning ResNet18
│   ├── assignment2_ollama/          # Python client for Ollama
│   └── assignment3_rag_gpt4all/     # RAG with GPT4ALL + FAISS
│
└── silver/
├── assignment1_autogpt/         # AutoGPT setup and notes
└── assignment2_autogen/         # AutoGen multi‑agent examples


---

## 🛠️ Environment Setup

### 1. Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\activate


### 2. Install dependencies

pip install -r requirements.txt


---

## 🧪 Gold Assignments

### **1. ResNet18 Fine‑Tuning**
Located in: `gold/assignment1_resnet/`

Includes:
- Transfer learning pipeline  
- Training and inference scripts  
- Notebook ready for Google Colab  

---

### **2. Python Client for Ollama**
Located in: `gold/assignment2_ollama/`

Includes:
- Minimal Python wrapper for local LLMs  
- Easy integration with any Ollama model  

---

### **3. RAG with GPT4ALL + FAISS**
Located in: `gold/assignment3_rag_gpt4all/`

Includes:
- Document chunking  
- Embedding generation  
- FAISS vector store  
- Local LLM inference with GPT4ALL  

---

## 🧠 Silver Assignments

### **1. AutoGPT**
Located in: `silver/assignment1_autogpt/`

Includes:
- Setup notes  
- Environment configuration  
- Execution workflow  

---

### **2. AutoGen Agents**
Located in: `silver/assignment2_autogen/`

Includes:
- Multi‑agent collaboration  
- Tool‑enabled agents  
- RAG‑enhanced reasoning  

---

## 🚀 Running the Project

### **Local Execution**
Use the Python scripts inside each assignment folder:

python train_resnet.py
python inference.py
python ollama_client.py
python rag_gpt4all.py


### **Google Colab**
All notebooks (`.ipynb`) are prepared to run on Colab with GPU support.

---

## 📌 Notes
- Datasets are **not included** in the repository.  
- GPT4ALL `.gguf` models must be downloaded manually.  
- FAISS indexes are generated locally.  
- The project is structured to be modular, reproducible, and easy to extend.

---

## 📫 Contact
If you have questions or want to collaborate, feel free to reach out.

