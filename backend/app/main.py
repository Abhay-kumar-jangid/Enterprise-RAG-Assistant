from app.api.chat import router as chat_router
from app.api.test_retriever import router as retriever_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router

app = FastAPI(
    title="Cross-Domain RAG Question Answering System",
    description="Backend API for a Retrieval-Augmented Generation System using Gemini",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(retriever_router)
app.include_router(upload_router)


@app.get("/")
async def home():
    return {
        "message": "Cross-Domain RAG Backend Running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "Healthy"
    }