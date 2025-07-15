import yaml

class Config:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            self.cfg = yaml.safe_load(f)

    def get_ollama(self):
        return self.cfg["ollama"]

    def get_qdrant(self):
        return self.cfg["qdrant"]
