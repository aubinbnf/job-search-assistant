# Exécuter Qdrant localement
docker run -d -p 6333:6333 -p 6334:6334 qdrant/qdrant

# Description de l'architecture du projet
project/
├── config.yaml
├── config.py
├── main.py             ← Script de test / usage
├── vectorizer.py       ← Gère l'embedding via Ollama
├── vectordb.py         ← Gère Qdrant (création, insertion, recherche)
├── chunker.py          ← Découpe les PDF  
