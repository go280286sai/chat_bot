"""
Category route
"""
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from src.model_data.get_model_category import CreateModel, UpdateModel
from src.models.categories_database import CategoriesDatabase

router = APIRouter()


@router.post("/create")
async def category_create(cat: CreateModel):
    """
    Create a new category
    :param cat:
    :return:
    """
    try:
        obj = CategoriesDatabase()
        result = obj.create(name=cat.name)
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
async def category_get(idx: int):
    """
    Get a specific category
    :param idx:
    :return:
    """
    try:
        obj = CategoriesDatabase()
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
async def category_update(idx: int, cat: UpdateModel):
    """
    Update a specific category
    :param idx:
    :param cat:
    :return:
    """
    try:
        obj = CategoriesDatabase()
        name = cat.name
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
async def category_gets():
    """
    Get all categories
    :return:
    """
    try:
        obj = CategoriesDatabase()
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
                "data": {"categories": result},
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
async def category_delete(idx: int):
    """
    Delete a specific category
    :param idx:
    :return:
    """
    try:
        obj = CategoriesDatabase()
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
