@echo off

:: Set environment variables
set BACKEND_PORT=8000
set FRONTEND_PORT=5500

:: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment. Please check your setup.
    pause
    exit /b
)

:: Install dependencies
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies. Please check your requirements.txt file.
    pause
    exit /b
)

:: Start backend
echo Starting backend on port %BACKEND_PORT%...
start cmd /k "cd backend && python api.py"
if %errorlevel% neq 0 (
    echo Failed to start backend. Please check for errors in api.py.
    pause
    exit /b
)

:: Wait for backend to initialize
timeout /t 5 /nobreak >nul

:: Start frontend
echo Starting frontend on port %FRONTEND_PORT%...
start cmd /k "cd frontend && python -m http.server %FRONTEND_PORT%"
if %errorlevel% neq 0 (
    echo Failed to start frontend. Please check for errors in frontend files.
    pause
    exit /b
)

:: Open in browser
echo Opening application in browser...
start "" "http://127.0.0.1:%FRONTEND_PORT%/home.html"

echo Application started successfully!
pause