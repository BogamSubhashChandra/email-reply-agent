import os
import requests

# ✅ DEFINE API KEY HERE
API_KEY = os.getenv("GEMINI_API_KEY")


def classify_email(email: str):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

    prompt = f"""
    Classify this email into one word:
    request, complaint, follow-up, appreciation, other

    Email:
    {email}
    """

    try:
        res = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })

        data = res.json()
        print("CLASSIFIER DEBUG:", data)

        if "candidates" not in data:
            return "other"

        return data["candidates"][0]["content"]["parts"][0]["text"].strip().lower()

    except Exception as e:
        print("Classifier error:", e)
        return "other"