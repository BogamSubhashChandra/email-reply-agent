from app.agents.classifier import classify_email
from app.agents.tone import detect_tone
from app.agents.reply import generate_reply
from app.agents.tasks import extract_tasks, is_meeting_task
from app.agents.priority import detect_priority

from app.db import SessionLocal
from app.models import Task
from app.integrations.slack import send_to_slack
from app.integrations.gmeet import create_meet_event

def process_email(email: str):
    intent = classify_email(email)
    tone = detect_tone(email)

    tasks = extract_tasks(email)

    db = SessionLocal()
    final_tasks = []
    meet_links = []

    for t in tasks:
        priority = detect_priority(t)

        db_task = Task(description=t, priority=priority)
        db.add(db_task)

        final_tasks.append({
            "task": t,
            "priority": priority
        })

        if is_meeting_task(t):
            link = create_meet_event(t)
            meet_links.append(link)

    db.commit()
    db.close()

    send_to_slack(tasks)

    reply = generate_reply(email, intent, tone)

    return {
        "intent": intent,
        "tone": tone,
        "tasks": final_tasks,
        "meet_links": meet_links,
        "reply": reply
    }