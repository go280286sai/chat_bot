"""
Test cases for questions_route_test.py
"""
from httpx import AsyncClient, ASGITransport
import pytest
from fastapi import status

from main import app
import pytest_asyncio

transport = ASGITransport(app=app)


@pytest_asyncio.fixture
async def client():
    """
    Fixture to make a test client fixture.
    :return:
    """
    async with AsyncClient(
            transport=transport,
            base_url="http://test"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_create_languages_route(client: AsyncClient):
    """
    Test cases for create_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/create",
                                 json={
                                     "name": "english"
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_create_categories_route(client: AsyncClient):
    """
    Test cases for create_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/create",
                                 json={
                                     "name": "Test Category",
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_create_questions_route(client: AsyncClient):
    """
    Test cases for create_questions_route
    :param client:
    :return:
    """
    response = await client.post("/api/questions/create",
                                 json={
                                     "name": "Test questions",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_create_questions_route_fail(client: AsyncClient):
    """
    Test cases for create_questions_route
    :param client:
    :return:
    """
    response = await client.post("/api/questions/create",
                                 json={
                                     "name": 1,
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_answers_route_fail_unique(client: AsyncClient):
    """
    Test cases for create_questions_route
    :param client:
    :return:
    """
    response = await client.post("/api/questions/create",
                                 json={
                                     "name": "Test questions",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_questions_route(client: AsyncClient):
    """
    Test cases for get_questions_route
    :param client:
    :return:
    """
    response = await client.get("/api/questions/get/1")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"]["id"] == 1
    assert body["data"]["name"] == "Test questions"
    assert body["data"]["language"] == "english"
    assert body["data"]["category"] == "Test Category"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_update_questions_route(client: AsyncClient):
    """
    Test cases for update_questions_route
    :param client:
    :return:
    """
    response = await client.post("/api/questions/update/1",
                                 json={
                                     "name": "Test questions new",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_gets_questions_route(client: AsyncClient):
    """
    Test cases for gets_questions_route
    :param client:
    :return:
    """
    response = await client.get("/api/questions/")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    for item in body["data"]['questions']:
        assert item["name"] == "Test questions new"
        assert item["language"] == "english"
        assert item["category"] == "Test Category"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_delete_questions_route(client: AsyncClient):
    """
    Test cases for delete_questions_route
    :param client:
    :return:
    """
    response = await client.post("/api/questions/delete/1")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_delete_languages_route(client: AsyncClient):
    """
    Test cases for delete_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/delete/1")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_delete_categories_route(client: AsyncClient):
    """
    Test cases for delete_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/delete/1")
    assert response.status_code == status.HTTP_200_OK
