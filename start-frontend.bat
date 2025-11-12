@echo off
REM start-frontend.bat — installs dependencies (if missing) and starts Vite dev server
SETLOCAL
cd /d "%~dp0frontend"
REM Install node modules if node_modules missing
IF NOT EXIST node_modules (
  echo Installing frontend dependencies...
  npm install
)
necho Starting Vite dev server on available port...
REM Use start /B to open in background, but keep the window for logs if executed manually.
npm run dev
ENDLOCAL
