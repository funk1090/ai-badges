import requests

class OllamaChatClient:
    def __init__(self, model="llama3", host="http://localhost:11434"):
        self.model = model
        self.url = f"{host}/api/chat"
        self.history = []  # chat history

    def ask(self, user_message: str) -> str:
        # Add user message to history
        self.history.append({"role": "user", "content": user_message})

        payload = {
            "model": self.model,
            "messages": self.history,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code != 200:
            raise RuntimeError(f"Ollama error: {response.text}")

        data = response.json()
        assistant_reply = data["message"]["content"]

        # Add assistant reply to history
        self.history.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply


if __name__ == "__main__":
    chat = OllamaChatClient(model="llama3")

    print("Chat started. Type 'exit' to escape.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        reply = chat.ask(user_input)
        print("Model:", reply)
