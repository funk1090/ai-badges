# main.py
from autogen import AssistantAgent, UserProxyAgent
from rag import add_document, query
import json

# --- 1. Función para limpiar texto UTF-16 ---

# --- 2. Cargar documento ---
with open("docs/sample.txt", "rb") as f:
    raw = f.read()

try:
    text = raw.decode("utf-16")
except:
    text = raw.decode("utf-8", errors="ignore")

add_document(text, metadata={"id": "sample"})

# --- 3. Ejecutar RAG manualmente ---
rag_results = query("What information is contained in the sample document?")

if rag_results:
    summary = rag_results[0]["text"]
else:
    summary = "No information found in the document."

# --- 4. Guardar memoria ---
with open("memory.json", "w", encoding="utf-8") as f:
    json.dump({"summary": summary}, f, indent=4, ensure_ascii=False)

# --- 5. Crear agentes ---
assistant = AssistantAgent(
    name="assistant",
    llm_config={
        "model": "llama3",
        "api_type": "ollama",
        "base_url": "http://localhost:11434",
        "temperature": 0.2
    }
)

user = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
)

# --- 6. Pasar el resumen al agente ---
goal = f"Here is the summary extracted from the document:\n\n{summary}\n\nUse this to continue the task."

# --- 7. Iniciar chat ---
user.initiate_chat(assistant, message=goal)
