from fastapi import FastAPI
from dotenv import load_dotenv
from app.schemas import EmailRequest, EmailResponse
from app.orchestrator import process_email

load_dotenv()

app = FastAPI(title="Email Reply Agent")

@app.get("/")
def root():
    return {"message": "Email Reply Agent Running 🚀"}

@app.post("/reply", response_model=EmailResponse)
def reply(req: EmailRequest):
    return process_email(req.email)