from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    question: str


class Source(BaseModel):
    filename: str
    page:int


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]