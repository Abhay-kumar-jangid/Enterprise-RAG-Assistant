from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    # Load model only once
    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    def embed_documents(self, texts):

        return self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

    def embed_query(self, query):

        return self.model.encode(
            query,
            convert_to_numpy=True
        )