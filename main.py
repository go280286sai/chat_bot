"""
Embedded chat for client consultation.
Operates in three languages: English, Russian, and Ukrainian.
"""
import uvicorn
from fastapi import FastAPI
from routes import index_route

app = FastAPI()

app.include_router(router=index_route.router, prefix="/api", tags=["api"])


@app.get("/")
def main():
    """
    Main function for chatbot.
    :return:
    """
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
