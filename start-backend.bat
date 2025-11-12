@echo off
REM start-backend.bat — creates/activates Python venv, installs requirements, and starts uvicorn
SETLOCAL
cd /d "%~dp0backend"
necho Ensuring Python virtual environment exists...
IF NOT EXIST .venv (
  python -m venv .venv
)
echo Activating virtual environment...
call .\.venv\Scripts\activate.bat
echo Installing backend requirements (if needed)...
pip install -r requirements.txt
echo Starting Uvicorn on port 8000...
REM Run uvicorn in the foreground so logs appear in this window
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
ENDLOCAL
