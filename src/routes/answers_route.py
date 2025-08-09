"""
Answers route
"""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from src.model_data.get_model_answer import CreateModel, UpdateModel
from src.models.answers_database import AnswersDatabase

router = APIRouter()


@router.post("/create")
async def answers_create(ans: CreateModel):
    """
    Create a new answers
    :param ans:
    :return:
    """
    try:
        obj = AnswersDatabase()
        result = obj.create(
            name=ans.name,
            language_id=ans.language_id,
            category_id=ans.category_id
        )
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Creation failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            })
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{idx}")
async def answers_get(idx: int):
    """
    Get a specific answers
    :param idx:
    :return:
    """
    try:
        obj = AnswersDatabase()
        result = obj.get_one(idx=int(idx))
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Getting failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": result,
                "error": False
            })
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{idx}")
async def answers_update(idx: int, ans: UpdateModel):
    """
    Update a specific answers
    :param ans:
    :param idx:
    :return:
    """
    try:
        obj = AnswersDatabase()
        name = ans.name
        result = obj.update(
            idx=int(idx),
            name=name,
            category_id=int(ans.category_id),
            language_id=int(ans.language_id)
        )
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Updating failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            })
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def answers_gets():
    """
    Get all answers
    :return:
    """
    try:
        obj = AnswersDatabase()
        result = obj.get_all()
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Getting failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"answers": result},
                "error": False
            })
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{idx}")
async def answers_delete(idx: int):
    """
    Delete a specific answers
    :param idx:
    :return:
    """
    try:
        obj = AnswersDatabase()
        result = obj.delete(idx=int(idx))
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Deleting failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            })
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
