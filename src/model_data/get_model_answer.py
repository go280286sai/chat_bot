from pydantic import BaseModel


class CreateModel(BaseModel):
    name: str
    category_id: int
    language_id: int


class UpdateModel(BaseModel):
    name: str
    category_id: int
    language_id: int
