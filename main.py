"""
Embedded chat for client consultation.
Operates in three languages: English, Russian, and Ukrainian.
"""
import uvicorn
from fastapi import FastAPI
from src.routes import (index_route, languages_route, questions_route,
                        categories_route, answers_route)
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename="logs.log", filemode='a+', datefmt='%d-%m-%y %H:%M:%S'
)
app = FastAPI()

app.include_router(router=index_route.router, prefix="/api/message", tags=["message"])
app.include_router(router=languages_route.router, prefix="/api/languages", tags=["languages"])
app.include_router(router=categories_route.router, prefix="/api/categories", tags=["categories"])
app.include_router(router=answers_route.router, prefix="/api/answers", tags=["answers"])
app.include_router(router=questions_route.router, prefix="/api/questions", tags=["questions"])


@app.get("/")
def main():
    """
    Main function for chatbot.
    :return:
    """
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
