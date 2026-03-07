# Email Reply Generator Agent

## Project Summary:
The Email Reply Generator Agent is an AI-powered service deployed on Google Cloud Run that automatically generates professional or customized email responses. Built with Python and FastAPI, it leverages Google’s Gemini model via the Generative AI API. Users send an email text and desired tone via a POST request to /generate-reply , and the agent returns structured suggested replies in JSON format. The project demonstrates serverless deployment, AI integration, and HTTP API design, making email response generation fast and automated. The Cloud Run endpoint is fully functional and accessible for testing.

## Overview
The Email Reply Generator Agent is an AI-powered system that automatically generates email replies. It accepts an input email text and a tone (e.g., professional, casual) and returns suggested email responses using Google’s Gemini model.

This project demonstrates deployment of an AI agent on **Google Cloud Run** with a simple HTTP interface.

---

## Features
- Accepts an email text and tone via POST request
- Generates professional or customized email replies using AI
- Returns responses in JSON format
- Fully serverless deployment on Cloud Run

---

## Tech Stack
- **Programming Language & Framework:** Python + FastAPI  
- **AI Model:** Google Gemini via Generative AI API  
- **Cloud Platform:** Google Cloud Run (serverless container deployment)  
- **Containerization:** Docker  
- **CLI Tools:** gcloud SDK, curl  
- **Editor:** VSCode (or any Python IDE)

---

## Deployment
The agent is deployed and publicly accessible at:

https://email-reply-agent-74784201301.europe-west1.run.app/generate-reply


---

## API Usage

### Endpoint
POST: /generate-reply



### Request Body
```json
{
  "email_text": "Hi team, can you send the Q1 report by Friday?",
  "tone": "professional"
}

### Response Example
```json
{
  "email_text": "Hi team, can you send the Q1 report by Friday?",
  "reply": "Depending on your progress with the report, here are a few ways to reply: ..."
}

Testing
Using Powershell:
$token = gcloud auth print-identity-token

curl -X POST "https://email-reply-agent-74784201301.europe-west1.run.app/generate-reply" `
-H "Authorization: Bearer $token" `
-H "Content-Type: application/json" `
-d '{ "email_text": "Hi team, can you send the Q1 report by Friday?", "tone": "professional" }'

Using cURl:
curl -X POST "https://email-reply-agent-74784201301.europe-west1.run.app/generate-reply" \
-H "Authorization: Bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{ "email_text": "Hi team, can you send the Q1 report by Friday?", "tone": "professional" }'


Project Structure:
email-reply-agent/
├─ main.py          # FastAPI server
├─ agent.py         # AI prompt & Gemini integration
├─ requirements.txt # Python dependencies
├─ Dockerfile       # Container setup
└─ README.md        # Project documentation


NOTES:
The agent only accepts POST requests to /generate-reply
Responses may include multiple options; you can modify the prompt in agent.py  to return a single clean reply.
Ensure you have Cloud Billing enabled and AI API access to run this project.


Submission:
Cloud Run Endpoint: https://email-reply-agent-74784201301.europe-west1.run.app/generate-reply
Repository: https://github.com/BogamSubhashChandra/email-reply-agent