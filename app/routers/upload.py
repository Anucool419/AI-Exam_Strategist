from fastapi import APIRouter, UploadFile, File
import os
from typing import List

router = APIRouter()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
@router.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    # Single file path
    # async def upload_file(file: UploadFile = File(...)):
    # file_path = os.path.join(UPLOAD_DIR, file.filename)

    # with open(file_path, "wb") as f:
    #     f.write(await file.read())

    # return {"message": "File uploaded successfully", "file_path": file_path}
    ### Multiple file paths
    file_paths = []

    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        file_paths.append(file_path)

    return {
        "message": "Files uploaded successfully",
        "file_paths": file_paths
    }