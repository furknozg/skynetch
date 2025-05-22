import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

API_KEY = os.getenv("API_KEY")
REPO_PATH = os.getenv("REPO_PATH", "data/flight_data.db")
