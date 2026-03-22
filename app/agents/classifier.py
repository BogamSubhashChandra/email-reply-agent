import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def classify_email(email: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"
    
    prompt = f"Classify this email: {email}"

    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    res = requests.post(url, json=body).json()

    # 🔥 DEBUG PRINT
    print("Classifier API Response:", res)

    # ✅ SAFE CHECK
    if "candidates" not in res:
        return "other"

    return res["candidates"][0]["content"]["parts"][0]["text"].strip().lower()