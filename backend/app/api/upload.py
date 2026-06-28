from app.services.rag_pipeline import RAGPipeline
from fastapi import APIRouter, UploadFile, File
from typing import List
import os
import shutil

from app.config import DOCUMENTS_DIR

router = APIRouter(
    prefix="/upload",
    tags=["Document Upload"]
)

pipeline = RAGPipeline()

@router.post("/")
async def upload_pdf(files: List[UploadFile] = File(...)):

    for file in files:

        if not file.filename.endswith(".pdf"):
            continue

        save_path = os.path.join(DOCUMENTS_DIR, file.filename)

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    pipeline.build_vector_database()

    return {
        "success": True,
        "message": f"{len(files)} document(s) uploaded and indexed successfully."
    }