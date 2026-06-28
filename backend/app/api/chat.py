from fastapi import APIRouter

from app.models.schemas import ChatRequest
from app.services.retriever import Retriever
from app.services.llm import GeminiLLM
from app.services.memory import ConversationMemory

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

llm = GeminiLLM()
memory = ConversationMemory()


@router.post("/")
async def chat(request: ChatRequest):

    retriever = Retriever()

    conversation = memory.get_context()

    retrieved_chunks = retriever.retrieve(
        request.question,
        top_k=5
    )

    answer = llm.generate_answer(
        request.question,
        retrieved_chunks,
        conversation
    )

    seen = set()
    sources = []

    for chunk in retrieved_chunks:

        key = (chunk["filename"], chunk["page"])

        if key not in seen:
            seen.add(key)

            sources.append({
                "filename": chunk["filename"],
                "page": chunk["page"]
            })

    memory.add(
        request.question,
        answer
    )

    return {
        "answer": answer,
        "sources": sources
    }