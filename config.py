# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Default to your provided backend URL (no trailing slash)
BACKEND_URL = os.getenv("BACKEND_URL", "https://petstagram-backend-v1.onrender.com")
