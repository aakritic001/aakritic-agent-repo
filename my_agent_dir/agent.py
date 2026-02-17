# agent.py
import os

class MyAgent:
    def __init__(self):
        self.api_key = os.environ.get("MY_SECRET_ENV_VAR") 
        print(f"Agent inited. Secret starts with: {self.api_key[:2] if self.api_key else 'None'}")

    def query(self, text: str) -> str:
        # Replace with your actual agent logic
        return f"Agent received: {text}. Secret in use: {bool(self.api_key)}"

# Vertex AI Needs this instantiated object to serve as the entrypoint!
agent_instance = MyAgent()
