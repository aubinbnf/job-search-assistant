import os
import requests

class OllamaVectorizer:
    def __init__(self, config):
        self.model = config["embedding_model"]
        self.url = os.getenv("OLLAMA_URL", config["url"])

    def embed(self, text):
        response = requests.post(
            f"{self.url}/api/embeddings",
            json={"model": self.model, "prompt": text}
        )
        response.raise_for_status()
        return response.json()["embedding"]
