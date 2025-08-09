from pydantic import BaseModel


class CreateModel(BaseModel):
    name: str


class UpdateModel(BaseModel):
    name: str
