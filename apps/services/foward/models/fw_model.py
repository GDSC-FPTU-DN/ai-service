from pydantic import BaseModel


class CreateFwDestinationModel(BaseModel):
    url: str = None


class DeleteFwDestinationModel(BaseModel):
    index: int = None
