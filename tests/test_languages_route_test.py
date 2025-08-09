"""
Test cases for languages_route_test.py
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
async def test_create_languages_route_fail(client: AsyncClient):
    """
    Test cases for create_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/create",
                                 json={
                                     "name": 1
                                 })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_languages_route_fail_unique(client: AsyncClient):
    """
    Test cases for create_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/create",
                                 json={
                                     "name": "english"
                                 })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_languages_route(client: AsyncClient):
    """
    Test cases for get_languages_route
    :param client:
    :return:
    """
    response = await client.get("/api/languages/get/1")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "english"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_update_languages_route(client: AsyncClient):
    """
    Test cases for update_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/update/1",
                                 json={
                                     "name": "english_"
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_gets_languages_route(client: AsyncClient):
    """
    Test cases for gets_languages_route
    :param client:
    :return:
    """
    response = await client.get("/api/languages/")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    for language in body["data"]['languages']:
        assert language["name"] == "english_"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_delete_languages_route(client: AsyncClient):
    """
    Test cases for delete_languages_route
    :param client:
    :return:
    """
    response = await client.post("/api/languages/delete/1")
    assert response.status_code == status.HTTP_200_OK
