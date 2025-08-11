"""
Test cases for languages_route_test.py
"""
from httpx import AsyncClient, ASGITransport
import pytest
from fastapi import status

from main import app
import pytest_asyncio

from src.app.main_chat import MainChat

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
async def test_create_demo_database(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.get("/api/demo/create")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is None


def test_main_chat():
    obj = MainChat()
    response = obj.get("Delivery", "en")
    assert response is not None
    response = obj.get("Доставка", "uk")
    assert response is not None
    response = obj.get("Оплата", "ru")
    assert response is not None


@pytest.mark.asyncio
async def test_delete_demo_database(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.get("/api/demo/delete")
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is None
    assert body["error"] is None
