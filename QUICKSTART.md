# Quick Start Guide - Study Agent

## 🚀 Get Started in 5 Minutes

### Step 1: Get Your API Key

**Option A: Google Gemini (Recommended)** ⭐
- Visit https://aistudio.google.com/app/apikey
- Click "Create API Key"
- Copy your key

**Option B: OpenAI** 
- Visit https://platform.openai.com/api-keys
- Create a new API key
- Copy your key

### Step 2: Configure Backend

You can run the full system with a cloud LLM (Google Gemini or OpenAI) or run a local demo without API keys using the included DummyLLM.

macOS / Linux (recommended when using cloud keys):

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# If using cloud LLMs, copy and edit the env file:
cp ../.env.example .env
# Edit .env and add your API key:
# GOOGLE_API_KEY=your_key_here
# OR
# OPENAI_API_KEY=your_key_here
```

PowerShell (Windows):

```powershell
cd backend

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# If using cloud LLMs, copy and edit the env file:
Copy-Item ..\.env.example .env
# Then open .env in your editor and set either GOOGLE_API_KEY or OPENAI_API_KEY
```

Quick demo without API keys (local, safe):

```powershell
# From backend/ with the venv activated
python demo_runner.py
```

This demo uses a tiny built-in DummyLLM that returns deterministic sample flashcards/quizzes so you can see the Reader, Flashcard, Quiz, and Planner agents in action without any API keys. Outputs are written to `backend/outputs`.

### Step 3: Start Backend

```bash
# From backend/ directory
uvicorn main:app --reload
```
✅ Backend running at http://localhost:8000

### Step 4: Setup Frontend

```bash
# In a new terminal, from frontend/ directory
npm install
npm run dev
```
✅ Frontend running at http://localhost:5173

### Step 5: Use the App

1. Open http://localhost:5173 in your browser
2. Upload a PDF document
3. Click "Generate All" to create flashcards, quizzes, and study plans
4. Chat about your study material

## 📋 Troubleshooting

### API Key Not Working?
```bash
# Check if key is set
echo $GOOGLE_API_KEY

# Or for OpenAI
echo $OPENAI_API_KEY
```

### Backend won't start?
```bash
# Activate venv first
source backend/.venv/bin/activate

# Then run
uvicorn main:app --reload
```

### Frontend shows 404 errors?
- Make sure backend is running on http://localhost:8000
- Check that backend/.env has your API key set

### "Module not found" errors?
```bash
# Reinstall backend dependencies
cd backend
pip install -r requirements.txt --force-reinstall
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload_pdf` | Upload a PDF file |
| POST | `/generate_all` | Generate flashcards, quizzes & planner |
| GET | `/flashcards` | Get flashcards |
| GET | `/quizzes` | Get quizzes |
| GET | `/planner` | Get study plan |
| POST | `/chat` | Ask questions |

## 📚 API Documentation

Once backend is running, visit: http://localhost:8000/docs

## 🔐 Security Reminder

- ⚠️ Never commit `.env` files to git
- 🔄 Rotate API keys if accidentally exposed
- 📁 All keys are listed in `.gitignore`

## 📱 Features

- ✅ PDF upload and processing
- ✅ AI flashcard generation
- ✅ Smart quiz creation
- ✅ Study scheduling
- ✅ Contextual chat
- ✅ Google Gemini & OpenAI support

## 🆘 Need Help?

Check the main README.md for detailed documentation and advanced configuration.
