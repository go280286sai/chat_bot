"""
Languages route
"""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from src.model_data.get_model_language import CreateModel, UpdateModel
from src.models.languages_database import LanguagesDatabase

router = APIRouter()


@router.post("/create")
async def languages_create(lang: CreateModel):
    """
    Create a new language
    :param lang:
    :return:
    """
    try:
        obj = LanguagesDatabase()
        result = obj.create(name=lang.name)
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
async def languages_get(idx: int):
    """
    Get a specific language
    :param idx:
    :return:
    """
    try:
        obj = LanguagesDatabase()
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
async def languages_update(idx: int, lang: UpdateModel):
    """
    Update a specific language
    :param idx:
    :param lang:
    :return:
    """
    try:
        obj = LanguagesDatabase()
        name = lang.name
        result = obj.update(idx=int(idx), name=name)
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
async def languages_gets():
    """
    Get all languages
    :return:
    """
    try:
        obj = LanguagesDatabase()
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
                "data": {"languages": result},
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
async def languages_delete(idx: int):
    """
    Delete a new language
    :param idx:
    :return:
    """
    try:
        obj = LanguagesDatabase()
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
