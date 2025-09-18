import os
from dotenv import load_dotenv
from agents.extensions.models.litellm_model import LitellmModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = LitellmModel(
    model="gemini/gemini-2.5-flash",
    base_url="https://generativelanguage.googleapis.com",
    api_key=api_key
)