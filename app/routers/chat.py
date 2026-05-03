from fastapi import APIRouter
from pydantic import BaseModel

from app.core.chat_agent import chat_with_system

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    context: dict

@router.post("/chat")
async def chat(request: ChatRequest):
    response = chat_with_system(request.query, request.context)

    return {"response": response}