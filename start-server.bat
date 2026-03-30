@echo off
echo ==========================================
echo   THE ROYAL COURT - BACKEND STARTUP
echo ==========================================
echo.
cd /d "%~dp0server"
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found in server/venv.
    echo Please ensure the venv is correctly set up.
    pause
    exit /b
)
echo [1/2] Activating Virtual Environment...
call venv\Scripts\activate.bat
echo [2/2] Starting FastAPI Server on port 8000...
echo.
uvicorn main:app --reload --port 8000
pause
