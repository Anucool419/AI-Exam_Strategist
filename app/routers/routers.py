from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

SYLLABUS_PATH = "data/syllabus.txt"

@router.post("/upload-syllabus")
async def upload_syllabus(file: UploadFile = File(...)):
    content = await file.read()

    with open(SYLLABUS_PATH, "wb") as f:
        f.write(content)

    return {"message": "Syllabus uploaded"}