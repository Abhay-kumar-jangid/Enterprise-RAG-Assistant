from app.services.rag_pipeline import RAGPipeline
from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.config import DOCUMENTS_DIR

router = APIRouter(
    prefix="/upload",
    tags=["Document Upload"]
)

pipeline = RAGPipeline()

@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        return {
            "success": False,
            "message": "Only PDF files are allowed."
        }

    save_path = os.path.join(DOCUMENTS_DIR, file.filename)

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pipeline.build_vector_database()
    
    return {
        "success": True,
        "filename": file.filename,
        "message": "PDF uploaded and indexed successfully."
    }