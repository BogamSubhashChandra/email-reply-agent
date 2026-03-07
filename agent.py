import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_email_reply(email_text: str, tone: str = "professional"):

    prompt = f"Write a {tone} reply to this email: {email_text}"

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": API_KEY
    }

    data = {
        "contents":[
            {
                "parts":[{"text":prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]