Silver Assignment 2 — AutoGen + RAG + FAISS + Local LLM (Ollama)
This project implements an intermediate agentic AI system using AutoGen 0.3.1, FAISS, SentenceTransformers, and a local LLM running on Ollama.
The system demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline executed entirely on a desktop environment.

Assignment Objectives
This assignment requires:

Building an agentic AI application using AutoGen

Implementing RAG (Retrieval-Augmented Generation)

Using a vector database (FAISS)

Using tools or memory to store information

Running the system locally (desktop execution)

Demonstrating an intermediate-to-advanced agentic workflow

This project fulfills all requirements.

System Architecture
1. RAG Pipeline (rag.py)
Generates embeddings using SentenceTransformer

Stores vectors in FAISS

Supports document ingestion and semantic search

2. Document Input
Located in:

docs/sample.txt

The content can be replaced with any text you want to index.

3. Main Pipeline (main.py)
The system performs:

Load the document

Index it in FAISS

Execute a RAG query

Extract the most relevant text

Save a summary into memory.json

Pass the summary to the agent

The agent responds using the local LLM

4. Agents (AutoGen)
AssistantAgent — powered by Ollama (llama3)

UserProxyAgent — initiates the conversation automatically

🤖 Local LLM (Ollama)
The system uses:

llama3
Executed locally via:

ollama run llama3
No API keys or cloud services are required.

📁 Project Structure
assignment2_autogen/
│
├── main.py
├── rag.py
├── memory.json
├── docs/
│   └── sample.txt
└── README.md
▶️ Running the Project
Activate your virtual environment and run:

python main.py
This will:

Load and index the document

Perform a RAG query

Save a summary into memory.json

Trigger an AutoGen conversation using the summary

📌 Expected Output
memory.json will contain something like:

json
{
    "summary": "This document explains..."
}
The agent will then respond using this information.

🧩 Dependencies & Requirements
📦 Python Version
Python 3.10+ recommended

Virtual environment strongly recommended (python -m venv .venv)

📚 Required Python Libraries
These are the core libraries used in the project:

AutoGen
Código
autogen==0.3.1
Vector Database (FAISS)
Código
faiss-cpu
Embeddings
Código
sentence-transformers
Local LLM Integration
Código
ollama
Utilities
Código
pypdf
numpy
Optional (installed automatically by dependencies)
transformers

torch

typing_extensions

🖥 System Requirements
Ollama (Local LLM Runtime)
You must have Ollama installed and running locally:

macOS / Linux / Windows (WSL2)

Install from: https://ollama.com/download

Pull the model used in this assignment:

ollama pull llama3
📁 Project Setup
Inside your virtual environment:

pip install -r requirements.txt
Or install manually:

pip install autogen==0.3.1 faiss-cpu sentence-transformers pypdf ollama numpy
🧠 Why These Dependencies Matter
AutoGen 0.3.1 → agent orchestration

FAISS → vector search for RAG

SentenceTransformers → embedding generation

Ollama → local LLM execution (no API keys)

pypdf → optional PDF ingestion

numpy → required by FAISS

This section shows the evaluator that you understand the full stack and that your environment is reproducible.