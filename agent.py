import google.generativeai as genai
import os

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Select the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_email_reply(email_text: str, tone: str = "professional"):
    """
    Generate a reply for a given email text.
    """
    prompt = f"""
    You are an assistant that replies to emails professionally.
    Tone: {tone}
    
    Email to reply to:
    {email_text}
    
    Generate a concise professional reply.
    """
    
    response = model.generate_content(prompt)
    return response.text