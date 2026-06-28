from fastapi import APIRouter
import os

from app.config import DOCUMENTS_DIR, VECTOR_DB_DIR

router = APIRouter(
    prefix="/clear",
    tags=["Knowledge Base"]
)


@router.post("/")
async def clear_knowledge_base():

    # Delete uploaded PDFs
    for file in os.listdir(DOCUMENTS_DIR):
        if file.endswith(".pdf"):
            os.remove(os.path.join(DOCUMENTS_DIR, file))

    # Delete FAISS index
    faiss_file = os.path.join(VECTOR_DB_DIR, "faiss.index")
    metadata_file = os.path.join(VECTOR_DB_DIR, "metadata.pkl")

    if os.path.exists(faiss_file):
        os.remove(faiss_file)

    if os.path.exists(metadata_file):
        os.remove(metadata_file)

    return {
        "success": True,
        "message": "Knowledge base cleared successfully."
    }