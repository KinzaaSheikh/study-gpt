import chainlit as cl

@cl.on_chat_start
async def main():
    await cl.Message(content="👋 Hi! Welcome to StudyGPT.").send()

@cl.on_message
async def handle_message(message: str):
    await cl.Message(content=f"You said: {message}").send()
