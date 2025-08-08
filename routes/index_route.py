"""
Api router for chatbot
"""
from html import escape
from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse
from model_data.get_model_data import GetModelData

router = APIRouter()


@router.post("/get")
async def get_message(body: GetModelData):
    """
    Get message
    :param body:
    :return:
    """
    try:
        message = escape(body.message)
        lang = body.lang
        if lang not in ['en', 'ru', 'uk']:
            raise HTTPException(status_code=400, detail="Lang not supported")
        return JSONResponse(
            {
                "status": True,
                "data": message,
                "error": None
            }
        )
    except HTTPException as e:
        return JSONResponse(
            {
                "status": e.status_code,
                "data": None,
                "error": e.detail
            }
        )
