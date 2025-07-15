import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

class QdrantDB:
    def __init__(self, config):
        self.collection_name = config["collection"]
        self.client = QdrantClient(url=config["url"])
        self.vector_size = config["vector_size"]

        # Création de collection si elle n'existe pas
        if self.collection_name not in [c.name for c in self.client.get_collections().collections]:
            self.client.recreate_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE)
            )

    def insert_documents(self, docs: list, embed_fn):
        """docs: list de dicts {"text": ..., "metadata": {...}}"""
        points = []
        for doc in docs:
            vector = embed_fn(doc["text"])
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector,
                    payload={"text": doc["text"], "metadata": doc["metadata"]}
                )
            )
        self.client.upsert(collection_name=self.collection_name, points=points)

    def search(self, query_vector, top_k):
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=top_k,
            with_payload=True
        )
