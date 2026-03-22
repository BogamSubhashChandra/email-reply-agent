from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class EmailResponse(BaseModel):
    intent: str
    tone: str
    reply: str