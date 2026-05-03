from fastapi import APIRouter, UploadFile, File
from app.core.pdf_processor import extract_text_from_pdf
import os

router = APIRouter()

SYLLABUS_FILE = "data/syllabus.pdf"
SYLLABUS_TEXT = "data/syllabus.txt"

@router.post("/upload-syllabus")
async def upload_syllabus(file: UploadFile = File(...)):
    with open(SYLLABUS_FILE, "wb") as f:
        f.write(await file.read())

    # extract text
    text = extract_text_from_pdf(SYLLABUS_FILE)

    with open(SYLLABUS_TEXT, "w", encoding="utf-8") as f:
        f.write(text)

    return {"message": "Syllabus uploaded and processed"}