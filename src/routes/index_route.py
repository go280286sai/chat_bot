"""
Api router for chatbot
"""
import logging
from html import escape
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from starlette import status

from src.model_data.get_model_data import GetModelData
from src.app.main_chat import MainChat
from src.app.singlenton import Singleton

router = APIRouter()


class Chat(metaclass=Singleton):
    def __init__(self):
        if not hasattr(self, 'main_chat') or self.main_chat is None:
            self.main_chat = MainChat()


@router.post("/get")
async def get_message(body: GetModelData):
    """
    Get a message
    :param body:
    :return:
    """
    try:
        message = escape(body.message)
        lang = body.lang
        if lang not in ['en', 'ru', 'uk']:
            raise HTTPException(status_code=400, detail="Lang not supported")
        obj = Chat()
        answer = obj.main_chat.get(message=message, lang=lang)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"answer": answer},
                "error": None
            }
        )
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            }
        )
