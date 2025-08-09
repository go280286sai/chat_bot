"""
Test cases for answers_route_test.py
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
async def test_create_answers_route(client: AsyncClient):
    """
    Test cases for create_answers_route
    :param client:
    :return:
    """
    response = await client.post("/api/answers/create",
                                 json={
                                     "name": "Test answer",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_create_answers_route_fail(client: AsyncClient):
    """
    Test cases for create_answers_route
    :param client:
    :return:
    """
    response = await client.post("/api/answers/create",
                                 json={
                                     "name": 1,
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_answers_route_fail_unique(client: AsyncClient):
    """
    Test cases for create_answers_route
    :param client:
    :return:
    """
    response = await client.post("/api/answers/create",
                                 json={
                                     "name": "Test answer",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_answers_route(client: AsyncClient):
    """
    Test cases for get_answers_route
    :param client:
    :return:
    """
    response = await client.get("/api/answers/get/1")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"]["id"] == 1
    assert body["data"]["name"] == "Test answer"
    assert body["data"]["language"] == "english"
    assert body["data"]["category"] == "Test Category"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_update_answers_route(client: AsyncClient):
    """
    Test cases for update_answers_route
    :param client:
    :return:
    """
    response = await client.post("/api/answers/update/1",
                                 json={
                                     "name": "Test answer new",
                                     "category_id": 1,
                                     "language_id": 1
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_gets_answers_route(client: AsyncClient):
    """
    Test cases for gets_answers_route
    :param client:
    :return:
    """
    response = await client.get("/api/answers/")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    for item in body["data"]['answers']:
        assert item["name"] == "Test answer new"
        assert item["language"] == "english"
        assert item["category"] == "Test Category"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_delete_answers_route(client: AsyncClient):
    """
    Test cases for delete_answers_route
    :param client:
    :return:
    """
    response = await client.post("/api/answers/delete/1")
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
