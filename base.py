import requests
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
import uuid

# -------- CONFIG --------
OLLAMA_URL = "http://localhost:11434"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "my_documents"
MODEL = "nomic-embed-text"  # ou "llama3", etc.

# -------- ÉTAPE 1 : Qdrant - Création collection (si non existante) --------
qdrant = QdrantClient(url=QDRANT_URL)

if COLLECTION_NAME not in [c.name for c in qdrant.get_collections().collections]:
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE)  # à ajuster selon ton modèle
    )

# -------- ÉTAPE 2 : Fonction embedding via Ollama --------
def embed_text(text):
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={"model": MODEL, "prompt": text}
    )
    response.raise_for_status()
    return response.json()["embedding"]

# -------- ÉTAPE 3 : Exemple d’insertion de texte --------
#documents = [
#    {"text": "La Tour Eiffel est un monument célèbre à Paris.", "metadata": {"lang": "fr"}},
#    {"text": "L’ADN est la molécule de l’hérédité.", "metadata": {"lang": "fr"}},
#]
#
#points = []
#for doc in documents:
#    vector = embed_text(doc["text"])
#    points.append(
#        PointStruct(
#            id=str(uuid.uuid4()),
#            vector=vector,
#            payload={
#                "text": doc["text"],
#                "metadata": doc["metadata"]
#            }
#        )
#    )
#
#qdrant.upsert(collection_name=COLLECTION_NAME, points=points)
#print("✅ Données vectorisées et stockées dans Qdrant.")

# -------- ÉTAPE 4 : Recherche dans la collection --------
query = "Quels sont les monuments célèbres à Paris ?"
query_vector = embed_text(query)

results = qdrant.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_vector,
    limit=3,
    with_payload=True
)

for hit in results:
    print(f"Score: {hit.score:.3f} | Texte : {hit.payload['text']}")
