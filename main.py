import os
from fastapi import FastAPI
from pydantic import BaseModel
from agent import generate_email_reply
import uvicorn

app = FastAPI()

class EmailRequest(BaseModel):
    email_text: str
    tone: str = "professional"

@app.get("/")
def home():
    return {"message": "Email Reply Generator Agent is running"}

@app.post("/generate-reply")
def generate_reply(req: EmailRequest):
    reply = generate_email_reply(req.email_text, req.tone)
    return {
        "email_text": req.email_text,
        "reply": reply
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
