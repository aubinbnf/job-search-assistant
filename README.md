# Démarrer l'environnement local

## Installer les dépendances
pip install -r requirements.txt

## Lancement des conteneurs

### Build (Si c'est la première éxecution)
docker compose up --build

#### Télécharger les modèles dans le conteneur Ollama
ollama pull nomic-embed-text

### Run (Si les conteneurs ont déjà été build auparavant)
docker compose up

# Description de l'architecture du projet
project/
├── config.yaml
├── config.py
├── main.py             ← Script de test / usage
├── vectorizer.py       ← Gère l'embedding via Ollama
├── vectordb.py         ← Gère Qdrant (création, insertion, recherche)
├── chunker.py          ← Découpe les PDF  
