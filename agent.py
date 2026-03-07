import os
import google.generativeai as genai

# configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_email_reply(email_text: str, tone: str = "professional"):

    prompt = f"""
    Write a {tone} email reply to the following message:

    {email_text}
    """

    response = model.generate_content(prompt)

    return response.text
