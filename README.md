# Study Agent - AI-Powered Learning Tool

A full-stack application that uses AI to help students study more effectively by generating flashcards, quizzes, and study plans from uploaded PDF documents.

## Features

- **PDF Upload & Processing**: Upload PDFs and automatically extract text and chunk it intelligently
- **Flashcard Generation**: AI-generated question-answer flashcards from study material
- **Quiz Generation**: Multiple-choice quizzes with auto-generated questions
- **Study Planning**: Smart study schedules with spaced repetition
- **Chat Interface**: Ask questions about uploaded materials
- **Multi-LLM Support**: Use Google Gemini or OpenAI as your LLM provider

## Tech Stack

### Backend
- **FastAPI** - REST API framework
- **LangChain** - LLM orchestration
- **FAISS** - Vector database for semantic search
- **Google Gemini API** / **OpenAI** - Language models
- **PyMuPDF** - PDF processing

### Frontend
- **React** - UI framework
- **Axios** - HTTP client
- **Vite** - Build tool

## Setup Instructions

### Prerequisites
- Python 3.9+
- Node.js 16+
- Either Google Gemini API key OR OpenAI API key

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   ```

   PowerShell (Windows):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Keys**
   
   **Option A: Google Gemini (Recommended)**
   ```bash
   # Get your API key from: https://aistudio.google.com/app/apikey
   export GOOGLE_API_KEY=your_key_here
   ```

   PowerShell (Windows):
   ```powershell
   # Get your API key from: https://aistudio.google.com/app/apikey
   $env:GOOGLE_API_KEY = 'your_key_here'
   ```

   **Option B: OpenAI (Fallback)**
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```

   PowerShell (Windows):
   ```powershell
   $env:OPENAI_API_KEY = 'your_key_here'
   ```

5. **Run the backend server**
   ```bash
   uvicorn main:app --reload
   ```

   PowerShell (Windows):
   ```powershell
   # If using virtualenv activation
   .\.venv\Scripts\Activate.ps1
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run development server**
   ```bash
   npm run dev
   ```
   The app will be available at `http://localhost:5173`

## API Endpoints

### File Upload
- **POST** `/upload_pdf` - Upload a PDF file
   ```bash
   curl -X POST -F "file=@document.pdf" http://localhost:8000/upload_pdf
   ```

   PowerShell (Windows) - using Invoke-RestMethod:
   ```powershell
   Invoke-RestMethod -Uri http://localhost:8000/upload_pdf -Method Post -Form @{ file = Get-Item 'document.pdf' }
   ```

### Generation
- **POST** `/generate_all` - Generate flashcards, quizzes, and planner
   ```bash
   curl -X POST http://localhost:8000/generate_all
   ```

   PowerShell (Windows):
   ```powershell
   Invoke-RestMethod -Uri http://localhost:8000/generate_all -Method Post
   ```

### Retrieval
- **GET** `/flashcards` - Get generated flashcards
- **GET** `/quizzes` - Get generated quizzes
- **GET** `/planner` - Get study plan

### Chat
- **POST** `/chat` - Chat about uploaded materials
   ```bash
   curl -X POST -H "Content-Type: application/json" \
      -d '{"question": "What is X?", "chat_history": []}' \
      http://localhost:8000/chat
   ```

   PowerShell (Windows):
   ```powershell
   $body = @{ question = 'What is X?'; chat_history = @() } | ConvertTo-Json
   Invoke-RestMethod -Uri http://localhost:8000/chat -Method Post -Body $body -ContentType 'application/json'
   ```

## Environment Variables

Create a `.env` file in the backend directory (copy from `.env.example`):

```env
# Google Gemini Configuration (Recommended)
GOOGLE_API_KEY=your_google_api_key_here

# OpenAI Configuration (Optional, used as fallback)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Custom FAISS index path
FAISS_INDEX_PATH=./outputs/faiss_index

# Optional: Custom LLM model
LLM_MODEL=gpt-4o-mini
```

## Project Structure

```
study_agent/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Configuration (git-ignored)
│   ├── .env.example           # Configuration template
│   ├── agents/
│   │   ├── chat_agent.py      # Conversational retrieval
│   │   ├── flashcard.py       # Flashcard generation
│   │   ├── quiz.py            # Quiz generation
│   │   ├── planner.py         # Study planning
│   │   └── reader.py          # PDF processing
│   ├── utils/
│   │   ├── google_llm.py      # Google Gemini wrapper
│   │   └── pdf_utils.py       # PDF utilities
│   └── outputs/               # Generated files & FAISS index
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main app component
│   │   ├── api.js             # API client
│   │   ├── main.jsx           # Entry point
│   │   ├── styles.css         # Global styles
│   │   └── components/
│   │       ├── Chat.jsx
│   │       ├── Flashcards.jsx
│   │       ├── Planner.jsx
│   │       ├── Quizzes.jsx
│   │       └── UploadPanel.jsx
│   ├── package.json
│   └── vite.config.js
└── .gitignore                  # Git ignore rules
```

## Security Notes

🔐 **Important:**
- Never commit `.env` files or API keys to version control
- Rotate API keys if accidentally exposed
- Use `.env.example` to document required variables
- For production, use environment variables or secret management tools

## Troubleshooting

### Import Errors
If you see import errors, ensure the virtual environment is activated:
```bash
source backend/.venv/bin/activate  # macOS/Linux
```

PowerShell (Windows):
```powershell
.\backend\.venv\Scripts\Activate.ps1
```

### Google API Errors
- Verify your API key is correct
- Check that the key has Generative AI access enabled
- Ensure the key is set in the environment: `echo $GOOGLE_API_KEY`

### FAISS Index Errors
- Delete `outputs/faiss_index` to reset the vector database
- Upload a PDF to rebuild the index

### Frontend Connection Issues
- Ensure backend is running on `http://localhost:8000`
- Check browser console for CORS errors
- Verify frontend is configured with correct API URL

## Development

### Backend Development
- Hot-reload is enabled with `--reload` flag
- Check API docs at `http://localhost:8000/docs`
- View logs in terminal

### Frontend Development
- Hot-reload is enabled by default in Vite
- Check browser DevTools for errors

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under MIT License. See LICENSE file for details.

## Support

For issues or questions, please open an issue on GitHub or contact the development team.

## Recent changes (added features)

The repository was recently extended with a lightweight demo and UI/UX improvements to make it easy to try the system without cloud API keys. Key additions:

- Demo runner: `backend/demo_runner.py` — runs a small local demo using a DummyLLM so you can generate flashcards, quizzes and a study plan without configuring cloud LLM keys.
- Sample PDF: `backend/sample.pdf` — a one-page sample used by the demo.
- Backend endpoint: `POST /run_demo` — triggers the demo runner from the server and returns a brief summary of outputs.
- Frontend: "Run Demo" button in the Upload panel — calls `/run_demo` and refreshes flashcards/quizzes/planner automatically.
- Difficulty tagging & filtering: quizzes now include a `difficulty` field (defaulted when missing) and the frontend quiz UI has filter buttons (All/Easy/Medium/Hard) to show only quizzes of a chosen difficulty.
- Tests: Basic pytest tests were added under `backend/tests/` to validate the demo runner, the `/run_demo` endpoint, and that quizzes receive a default difficulty.

These changes are intended to make it easier to demo and test the system locally. For production usage with real LLMs, follow the original setup above and set your Google/OpenAI API keys in `backend/.env`.

## Changed code highlights

Below are short excerpts and descriptions of the most significant edits. They are meant to help reviewers quickly locate and understand the modifications.

- Demo runner (new file) — `backend/demo_runner.py`:

   - Purpose: standalone demo using a DummyLLM when no cloud keys are set.
   - Key snippet (creating dummy LLM & running agents):

      ```py
      class DummyLLM:
            def predict(self, prompt: str) -> str:
                  return json.dumps([...])  # simple deterministic Q/A or MCQ

      # Usage
      flash = FlashcardAgent(llm=DummyLLM())
      quizzes = quiz.generate_from_chunks(chunks)
      ```

- New backend endpoint — `POST /run_demo` in `backend/main.py`:

   - Purpose: run the demo runner from the server and return a summary of outputs.
   - Key snippet:

      ```py
      @app.post('/run_demo')
      async def run_demo():
            spec = importlib.util.spec_from_file_location('demo_runner', demo_path)
            demo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(demo)
            demo.main()  # saves outputs to ./outputs
            return { 'status': 'ok', 'summary': {...} }
      ```

- Quiz difficulty tagging — `backend/agents/quiz.py`:

   - Purpose: ensure every quiz object includes a `difficulty` field so the UI can filter reliably.
   - Key snippet (adding default difficulty after parsing):

      ```py
      parsed = json.loads(text)
      for item in parsed:
            if isinstance(item, dict) and 'difficulty' not in item:
                  item['difficulty'] = 'Medium'
      ```

- Frontend filtering UI — `frontend/src/components/Quizzes.jsx`:

   - Purpose: allow the student to filter displayed quizzes by difficulty (All/Easy/Medium/Hard).
   - Key snippet:

      ```jsx
      const [filter, setFilter] = useState('All');
      const filtered = quizzes.filter(q => (q.difficulty || 'Medium').toLowerCase() === filter.toLowerCase());
      <button onClick={() => setFilter('Easy')}>Easy</button>
      ```



   Meet the Team Behind Study_Agent:<br>
   1)Sreeramadasu Mukunda Rama Chary<br>       
   2)Yaswanth B<br>                                                        
   3)Boyinapalli Bhargav Venkata Dora<br>             
   4)Anegouni Swaranjith Kumar Goud<br>
                   

