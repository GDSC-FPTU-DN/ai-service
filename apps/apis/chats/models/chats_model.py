from pydantic import BaseModel, Field


class ChatsModel(BaseModel):
    prompt: str = Field(..., example="Hello, I'm a chatbot")
