"""
Data model for chatbot
"""
from pydantic import BaseModel


class GetModelData(BaseModel):
    """
    Data model for chatbot: Get message
    """
    lang: str
    message: str
