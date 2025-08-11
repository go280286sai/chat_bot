"""
Api router for demo chatbot
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from src.models.languages_database import LanguagesDatabase
from src.models.categories_database import CategoriesDatabase
from src.models.answers_database import AnswersDatabase
from src.models.questions_database import QuestionsDatabase
import pandas as pd

router = APIRouter()


@router.get("/create")
async def create_body():
    """
    Create database
    :return:
    """
    try:
        languages = pd.read_csv("files/languages.csv")
        languages_data = languages['languages_id'].values
        languages_database = LanguagesDatabase()
        for item in languages_data:
            languages_database.create(item)
        categories = pd.read_csv("files/category.csv", sep=';')
        categories_data = categories['category'].values
        categories_database = CategoriesDatabase()
        for item in categories_data:
            categories_database.create(item)
        answers = pd.read_csv("files/answers.csv", sep=";")
        answers_data = answers[
            ["answers",
             "category_id",
             "languages_id"]
        ].values
        answers_database = AnswersDatabase()
        for item in answers_data:
            answers_database.create(item[0], item[1], item[2])
        questions = pd.read_csv("files/questions.csv", sep=";")
        questions_data = questions[
            ["questions",
             "category_id",
             "languages_id"]
        ].values
        questions_database = QuestionsDatabase()
        for item in questions_data:
            questions_database.create(item[0], item[1], item[2])
        return JSONResponse(
            {
                "success": True,
                "data": None,
                "error": None
            }
        )
    except HTTPException as e:
        return JSONResponse(
            {
                "success": e.status_code,
                "data": None,
                "error": e.detail
            }
        )


@router.get("/delete")
async def delete_body():
    """
    Delete database
    :return:
    """
    try:
        answers_database = AnswersDatabase()
        answers_data = answers_database.get_all()
        for item in answers_data:
            answers_database.delete(item['id'])
        questions_database = QuestionsDatabase()
        questions_data = questions_database.get_all()
        for item in questions_data:
            questions_database.delete(item['id'])
        languages_database = LanguagesDatabase()
        languages_data = languages_database.get_all()
        for item in languages_data:
            languages_database.delete(item['id'])
        categories_database = CategoriesDatabase()
        categories_data = categories_database.get_all()
        for item in categories_data:
            categories_database.delete(item['id'])
        return JSONResponse(
            {
                "success": True,
                "data": None,
                "error": None
            }
        )
    except HTTPException as e:
        return JSONResponse(
            {
                "success": e.status_code,
                "data": None,
                "error": e.detail
            }
        )
