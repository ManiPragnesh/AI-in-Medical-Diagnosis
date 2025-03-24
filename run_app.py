import os
import subprocess
import webbrowser
import time
import sys

# Define constants
BACKEND_PORT = 8000
FRONTEND_PORT = 5500
VENV_DIR = "venv"

def activate_virtual_env():
    """Activates the virtual environment."""
    if not os.path.exists(VENV_DIR):
        print("Virtual environment not found. Creating...")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    activate_script = os.path.join(VENV_DIR, "Scripts", "activate.bat") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "activate")
    print("Activating virtual environment...")
    return [activate_script]

def install_dependencies():
    """Installs required dependencies from requirements.txt."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def start_backend():
    """Starts the backend server."""
    print("Starting backend...")
    backend_process = subprocess.Popen([sys.executable, "backend/api.py"], shell=True)
    return backend_process

def start_frontend():
    """Starts the frontend server."""
    print("Starting frontend...")
    os.chdir("frontend")
    frontend_process = subprocess.Popen([sys.executable, "-m", "http.server", str(FRONTEND_PORT)], shell=True)
    os.chdir("..")
    return frontend_process

def open_browser():
    """Opens the application in the default browser."""
    print("Opening application in browser...")
    webbrowser.open(f"http://127.0.0.1:{FRONTEND_PORT}/home.html")

if __name__ == "__main__":
    print("Setting up the application...")

    # Activate virtual environment and install dependencies
    activate_commands = activate_virtual_env()
    subprocess.run(activate_commands, shell=True)
    install_dependencies()

    # Start backend and frontend
    backend = start_backend()
    time.sleep(5)  # Allow backend time to initialize
    frontend = start_frontend()

    # Open the application in the browser
    open_browser()

    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("\nShutting down...")
        backend.terminate()
        frontend.terminate()