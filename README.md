# Exécuter Qdrant localement
docker run -d -p 6333:6333 -p 6334:6334 qdrant/qdrant

# Description de l'architecture du projet
project/
├── vectorizer.py      ← Gère l'embedding via Ollama
├── vectordb.py        ← Gère Qdrant (création, insertion, recherche)
├── main.py            ← Script de test / usage

