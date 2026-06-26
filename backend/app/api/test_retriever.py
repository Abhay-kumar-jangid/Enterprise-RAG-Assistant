from fastapi import APIRouter

from app.services.retriever import Retriever

router = APIRouter(
    prefix="/test",
    tags=["Testing"]
)

retriever = Retriever()


@router.get("/retrieve")
async def retrieve(question: str):

    return retriever.retrieve(question)