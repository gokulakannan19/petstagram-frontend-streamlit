# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# Set BACKEND_URL in .env or replace directly below
BACKEND_URL = os.getenv("BACKEND_URL", "https://your-backend.onrender.com")
