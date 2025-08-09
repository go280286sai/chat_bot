"""
Questions route
"""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from src.model_data.get_model_questions import CreateModel, UpdateModel
from src.models.questions_database import QuestionsDatabase

router = APIRouter()


@router.post("/create")
async def questions_create(ques: CreateModel):
    """
    Create a new questions
    :param ques:
    :return:
    """
    try:
        obj = QuestionsDatabase()
        result = obj.create(
            name=ques.name,
            language_id=ques.language_id,
            category_id=ques.category_id
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
async def questions_get(idx: int):
    """
    Get a specific questions
    :param idx:
    :return:
    """
    try:
        obj = QuestionsDatabase()
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
async def questions_update(idx: int, ques: UpdateModel):
    """
    Update a specific questions
    :param ques:
    :param idx:
    :return:
    """
    try:
        obj = QuestionsDatabase()
        name = ques.name
        result = obj.update(
            idx=int(idx),
            name=name,
            category_id=int(ques.category_id),
            language_id=int(ques.language_id)
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
async def questions_gets():
    """
    Get all questions
    :return:
    """
    try:
        obj = QuestionsDatabase()
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
                "data": {"questions": result},
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
async def questions_delete(idx: int):
    """
    Delete a specific questions
    :param idx:
    :return:
    """
    try:
        obj = QuestionsDatabase()
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
