import faiss
import numpy as np
import pickle
import os

from app.config import VECTOR_DB_DIR


class VectorStore:

    def __init__(self):

        self.index = None
        self.metadata = []

    def create_index(self, embeddings, metadata):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings.astype("float32"))

        self.metadata = metadata

    def save(self):

        faiss.write_index(
            self.index,
            os.path.join(VECTOR_DB_DIR, "faiss.index")
        )

        with open(
            os.path.join(VECTOR_DB_DIR, "metadata.pkl"),
            "wb"
        ) as f:

            pickle.dump(self.metadata, f)

    def load(self):

        self.index = faiss.read_index(
            os.path.join(VECTOR_DB_DIR, "faiss.index")
        )

        with open(
            os.path.join(VECTOR_DB_DIR, "metadata.pkl"),
            "rb"
        ) as f:

            self.metadata = pickle.load(f)

    def search(self, query_embedding, top_k=5):

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        results = []

        for distance, index in zip(distances[0], indices[0]):

            if index == -1:
                continue

            results.append({
                "score": float(distance),
                "filename": self.metadata[index]["filename"],
                "page":self.metadata[index]["page"],
                "content": self.metadata[index]["content"]
            })

        return results   