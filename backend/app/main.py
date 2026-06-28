from app.api.chat import router as chat_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router
from app.api.clear import router as clear_router

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
app.include_router(upload_router)
app.include_router(clear_router)


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