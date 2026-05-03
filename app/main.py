from fastapi import FastAPI
from app.routers import upload, analyze, planner, chat, qa, syllabus

app = FastAPI()

app.include_router(upload.router)
app.include_router(syllabus.router)
app.include_router(analyze.router)
app.include_router(planner.router)
app.include_router(chat.router)
app.include_router(qa.router)
from app.routers import eval
app.include_router(eval.router)