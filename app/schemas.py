from pydantic import BaseModel
from typing import List



class TaskItem(BaseModel):
    task: str
    priority: str




class EmailRequest(BaseModel):
    email: str


class EmailResponse(BaseModel):
    intent: str
    tone: str
    tasks: List[TaskItem]
    meet_links: List[str]
    reply: str