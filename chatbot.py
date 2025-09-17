import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

@cl.on_app_startup()
async def start():
    agent = Agent(
        name = "Assisstant",
        instructions = "You are a study tutor",
        model = LitellmModel(
            model="gemini/gemini-1.5-flash",
            base_url="https://generativelanguage.googleapis.com",
            api_key=api_key
        )
    )