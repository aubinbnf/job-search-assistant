from config import Config
from vectorizer import OllamaVectorizer
from vectordb import QdrantDB
from chunker import PDFChunker

cfg = Config()
ollama_cfg = cfg.get_ollama()
qdrant_cfg = cfg.get_qdrant()
chunker_cfg = cfg.get_chunker()

# Init services
vectorizer = OllamaVectorizer(ollama_cfg)
db = QdrantDB(qdrant_cfg)
chunker = PDFChunker(chunker_cfg)

# Exemple d'insertion
#docs = [
#    {"text": "La Tour Eiffel est un monument célèbre à Paris.", "metadata": {"lang": "fr"}},
#    {"text": "L’ADN est la molécule de l’hérédité.", "metadata": {"lang": "fr"}},
#]
pdf_chunks = chunker.chunk_pdf("Document.pdf")
db.insert_documents(pdf_chunks, vectorizer.embed)
print("✅ Données vectorisées et stockées dans Qdrant.")

# Recherche
query = "Quels sont les monuments célèbres à Paris ?"
query_vector = vectorizer.embed(query)
results = db.search(query_vector, top_k=3)

# Affichage
for hit in results:
    print(f"Score: {hit.score:.3f} | Texte : {hit.payload['text']}")
