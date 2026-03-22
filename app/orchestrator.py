from app.agents.classifier import classify_email
from app.agents.tone import detect_tone
from app.agents.reply import generate_reply

def process_email(email: str):
    intent = classify_email(email)
    tone = detect_tone(email)
    reply = generate_reply(email, intent, tone)

    return {
        "intent": intent,
        "tone": tone,
        "reply": reply
    }