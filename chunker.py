import fitz
import re
from typing import List

class PDFChunker:
    def __init__(self, config):
        self.chunk_size = config["chunk_size"]
        self.overlap = config["chunk_overlap"]

    def extract_text_from_pdf(self, file_path: str) -> List[str]:
        doc = fitz.open(file_path)
        pages = []
        for page_num, page in enumerate(doc):
            text = page.get_text()
            if text.strip():
                pages.append({"text": text.strip(), "page": page_num + 1})
        return pages

    def chunk_text(self, text: str) -> List[str]:
        # Nettoyage et découpage simple par tokens
        sentences = re.split(r'(?<=[\.\!\?])\s+', text)
        chunks = []
        current_chunk = []

        for sentence in sentences:
            current_chunk.append(sentence)
            if sum(len(s) for s in current_chunk) > self.chunk_size:
                chunk = " ".join(current_chunk)
                chunks.append(chunk)
                # Réutiliser les dernières phrases pour overlap
                current_chunk = current_chunk[-(self.overlap // 100):]

        # Ajouter le dernier chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def chunk_pdf(self, file_path: str) -> List[dict]:
        pages = self.extract_text_from_pdf(file_path)
        chunks = []

        for page in pages:
            for chunk in self.chunk_text(page["text"]):
                chunks.append({
                    "text": chunk,
                    "metadata": {
                        "page": page["page"],
                        "source": file_path
                    }
                })

        return chunks
