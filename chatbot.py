import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models import litellm_provider, litellm_model


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = litellm_provider()

@cl.on_chat_start
async def start():
    agent = Agent(
        name = "Assisstant",
        instructions = "You are a study tutor"
    )