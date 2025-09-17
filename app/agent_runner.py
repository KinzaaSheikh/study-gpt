from pydantic import BaseModel
from agents import Agent, Runner

class StudyOutput(BaseModel):
    answer: str
    mode: str



