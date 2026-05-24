# Silver Assignment 1 — AutoGPT Setup Notes

This document contains the setup instructions, configuration details, and execution notes for running **AutoGPT** in a local environment.

The goal of this assignment is to understand how autonomous agents operate, how they plan tasks, and how they interact with tools and external resources.

---

## 📌 1. Environment Setup

### **Create and activate a virtual environment**

python -m venv .venv
.venv\Scripts\activate


### **Install dependencies**

AutoGPT typically requires:

- Python 3.10+
- `openai` or compatible LLM provider
- `requests`
- `python-dotenv`
- Optional: Docker (for advanced features)

Install dependencies:

pip install -r requirements.txt


---

## 📌 2. AutoGPT Installation

### **Option A — Install via pip**

pip install autogpt


### **Option B — Clone the official repository**

git clone https://github.com/Significant-Gravitas/AutoGPT.git (github.com in Bing)
cd AutoGPT
pip install -r requirements.txt


---

## 📌 3. API Keys (if required)

Depending on the agent configuration, you may need:

- OpenAI API key  
- Azure OpenAI key  
- Local LLM endpoint (e.g., Ollama, GPT4ALL, LM Studio)

Create a `.env` file:

OPENAI_API_KEY=your_key_here

Or configure a local model:

LLM_PROVIDER=local
LLM_ENDPOINT=http://localhost:11434


---

## 📌 4. Running AutoGPT

### **Basic execution**

autogpt


Or, if using the cloned repo:

python -m autogpt


You will be prompted to:

- Name your agent  
- Define its role  
- Provide goals  
- Approve or deny actions  

---

## 📌 5. Notes on Autonomous Behavior

AutoGPT can:

- Plan multi‑step tasks  
- Search the web  
- Write files  
- Execute commands  
- Use memory (vector stores)  
- Iterate until goals are completed  

Be aware:

- Some actions may require manual approval  
- Some tasks may loop if goals are unclear  
- Costs may apply if using cloud LLMs  

---

## 📌 6. Recommended Experiments

- Create a research agent  
- Build a file‑writing agent  
- Use a local LLM instead of OpenAI  
- Enable vector memory  
- Test long‑horizon planning  

---

## 📌 7. Limitations

- Autonomous agents may hallucinate steps  
- They may attempt unnecessary actions  
- Local models may reduce reasoning quality  
- Requires careful goal definition  

---

## 📌 8. Conclusion

This assignment provides hands‑on experience with autonomous AI systems.  
Understanding AutoGPT is essential before moving into more advanced agent frameworks such as **AutoGen**, which is covered in the next assignment.

