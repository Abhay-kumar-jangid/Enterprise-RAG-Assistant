from fastapi import APIRouter
from app.services.memory import ConversationMemory
from app.models.schemas import ChatRequest
from app.services.retriever import Retriever
from app.services.llm import GeminiLLM

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

retriever = Retriever()
llm = GeminiLLM()
memory = ConversationMemory()


@router.post("/")
async def chat(request: ChatRequest):

    retrieved_chunks = retriever.retrieve(
        request.question,
        top_k=5
    )

    conversation = memory.get_context()

    search_query = conversation + "\nUser: " + request.question

    retrieved_chunks = retriever.retrieve(
        search_query,
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
    return{
        "answer":answer,
        "sources":sources
    }