from fastapi import APIRouter
from app.core.question_generator import generate_questions
router = APIRouter()

@router.get("/practice")
async def practice(topic: str):
    questions = generate_questions(topic)
    return {"questions": questions}