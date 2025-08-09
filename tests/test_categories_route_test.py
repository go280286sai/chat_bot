"""
Test cases for categories_route_test.py
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
async def test_create_categories_route_fail(client: AsyncClient):
    """
    Test cases for create_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/create",
                                 json={
                                     "name": 1
                                 })
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_create_categories_route_fail_unique(client: AsyncClient):
    """
    Test cases for create_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/create",
                                 json={
                                     "name": "Test Category"
                                 })
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_get_categories_route(client: AsyncClient):
    """
    Test cases for get_categories_route
    :param client:
    :return:
    """
    response = await client.get("/api/categories/get/1")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"]["name"] == "Test Category"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_update_categories_route(client: AsyncClient):
    """
    Test cases for update_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/update/1",
                                 json={
                                     "name": "Test Category New",
                                 })
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is False


@pytest.mark.asyncio
async def test_gets_categories_route(client: AsyncClient):
    """
    Test cases for gets_categories_route
    :param client:
    :return:
    """
    response = await client.get("/api/categories/")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    for language in body["data"]['categories']:
        assert language["name"] == "Test Category New"
    assert body["error"] is False


@pytest.mark.asyncio
async def test_delete_categories_route(client: AsyncClient):
    """
    Test cases for delete_categories_route
    :param client:
    :return:
    """
    response = await client.post("/api/categories/delete/1")
    assert response.status_code == status.HTTP_200_OK
