from fastapi import FastAPI
from dotenv import load_dotenv
from app.schemas import EmailRequest, EmailResponse
from app.orchestrator import process_email
from app.models import Base
from app.db import engine

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Smart Email Copilot Running 🚀"}

@app.post("/reply", response_model=EmailResponse)
def reply(req: EmailRequest):
    return process_email(req.email)