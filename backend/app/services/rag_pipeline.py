from app.config import DOCUMENTS_DIR
from app.services.pdf_loader import PDFLoader
from app.services.chunker import DocumentChunker
from app.services.embedding import EmbeddingModel
from app.services.vector_store import VectorStore


class RAGPipeline:

    def __init__(self):

        self.loader = PDFLoader()

        self.chunker = DocumentChunker()

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

    def build_vector_database(self):

        print("Loading documents...")

        documents = self.loader.load_documents(DOCUMENTS_DIR)

        print(f"{len(documents)} documents loaded.")

        chunks = self.chunker.chunk_documents(documents)

        print(f"{len(chunks)} chunks created.")

        texts = [chunk["content"] for chunk in chunks]

        embeddings = self.embedding_model.embed_documents(texts)

        self.vector_store.create_index(
            embeddings,
            chunks
        )

        self.vector_store.save()

        print("Vector database created successfully.")