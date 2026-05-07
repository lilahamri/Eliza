import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

MODEL = "ministral-3b"

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

# Tokens max 
STUDENT_MAX_TOKENS = 600
TEACHER_MAX_TOKENS = 600


DISCORD_TOKEN = os.getenv("TOKEN")