from pydantic import BaseModel
from agents import Agent, Runner
from model_adapter import model

class StudyOutput(BaseModel):
    answer: str
    mode: str

def study_agent():
    instructions = """
        You are Study GPT: your modes are:
        - explain: provide an intuitive explanation, short examples, and a one-sentence summary.
        - flashcards: produce 5 question/answer flashcards in JSON format.
        - quiz: give 5 multiple-choice questions and mark correct answers hiddenly.
        - spaced_repetition: suggest an SM-2 schedule and the next review date.
        Be concise, use step-by-step examples, and ask follow-up questions for clarity.
    """
    agent = Agent(
        name = "Study GPT",
        instructions = instructions,
        output_type= StudyOutput,
        model = model
    )

    # def run_mode(mode: str, prompt: str):
    #     agent = study_agent()
    #     runner = Runner()
    #     input_text = f"Mode: {mode}\nUser prompt: {prompt}"
    #     result = runner.run_sync(agent, input_text)
    #     return result.final_output