import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")


def generate_reply(email: str, intent: str, tone: str):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

    prompt = f"""
    You are an AI email assistant.

    Email:
    {email}

    Generate a short professional reply.
    Keep it clear and polite.
    """

    try:
        res = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })

        data = res.json()
        print("REPLY DEBUG:", data)

        if "candidates" not in data:
            return "I will get back to you shortly."

        return data["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        print("Reply error:", e)
        return "Unable to generate reply"