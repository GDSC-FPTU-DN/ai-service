from pydantic import BaseModel, Field


class ChatsModel(BaseModel):
    prompt: str = Field(..., example="Hello, I'm a chatbot")
    histories: list[dict[str, str]] | None = Field(
        None, example=[{"user": "Hello", "assistant": "Hi"}])
