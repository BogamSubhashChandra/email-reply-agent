import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_reply(email: str, intent: str, tone: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

    prompt = f"Reply to this email: {email}"

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    res = requests.post(url, json=body).json()

    # 🔥 DEBUG PRINT
    print("Reply API Response:", res)

    # ✅ SAFE CHECK
    if "candidates" not in res:
        return "Sorry, unable to generate reply right now."

    return res["candidates"][0]["content"]["parts"][0]["text"].strip()