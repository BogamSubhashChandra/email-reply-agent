def detect_tone(email: str) -> str:
    email = email.lower()

    if "urgent" in email or "asap" in email:
        return "strict"
    elif "thanks" in email or "please" in email:
        return "friendly"
    else:
        return "professional"