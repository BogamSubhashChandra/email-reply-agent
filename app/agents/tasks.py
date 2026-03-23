import os
import requests
import json

API_KEY = os.getenv("GEMINI_API_KEY")


def extract_tasks(email: str):
    """
    Extract tasks using Gemini
    """
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash-lite:generateContent?key={API_KEY}"

    prompt = f"""
    Extract actionable tasks from the email.

    Email:
    {email}

    Return ONLY JSON array.
    Example:
    ["Submit report", "Schedule meeting"]
    """

    try:
        res = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })

        data = res.json()
        print("TASK DEBUG:", data)

        if "candidates" not in data:
            return []

        text = data["candidates"][0]["content"]["parts"][0]["text"]

        # Try parsing JSON
        try:
            return json.loads(text)
        except:
            # fallback parsing
            text = text.replace("[", "").replace("]", "").replace('"', "")
            tasks = text.split(",")
            return [t.strip() for t in tasks if t.strip()]

    except Exception as e:
        print("Task error:", e)
        return []


def is_meeting_task(task: str):
    """
    Detect if task requires meeting
    """
    keywords = [
        "meeting",
        "call",
        "discussion",
        "meet",
        "zoom",
        "sync"
    ]

    task_lower = task.lower()

    return any(k in task_lower for k in keywords)