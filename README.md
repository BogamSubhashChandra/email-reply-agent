# 🚀 Smart Email Copilot AI Agent

AI-powered backend agent that transforms emails into actionable workflows:
- 📩 Understands email intent
- 🧠 Detects tone
- ✅ Extracts tasks
- 🚨 Detects priority
- 📅 Schedules Google Meet
- ✉️ Generates reply

---

## 🔥 Features

- Intent classification using Gemini
- Tone detection
- Task extraction from emails
- Priority detection (High / Medium / Low)
- Google Meet link generation
- REST API endpoint (`/reply`)
- SQLite database for task storage

---

## 🧠 Architecture

Email Input  
→ Intent Classifier  
→ Tone Detector  
→ Task Extractor  
→ Priority Detector  
→ Google Meet Generator  
→ Reply Generator  
→ JSON Response  

---

## ⚙️ Tech Stack

- Python 3.11
- FastAPI
- Gemini API (Google AI)
- SQLite (SQLAlchemy)
- Google Calendar API
- Uvicorn

---

