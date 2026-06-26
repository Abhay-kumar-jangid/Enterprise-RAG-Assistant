from app.services.embedding import EmbeddingModel
from app.services.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

        self.vector_store.load()

    def retrieve(self, question: str, top_k: int = 5):

        query_embedding = self.embedding_model.embed_query(question)

        results = self.vector_store.search(
            query_embedding,
            top_k
        )

        return results