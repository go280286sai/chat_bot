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


@pytest.mark.asyncio
async def test_get_message_en(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.post("/api/message/get",
                                 json={"message": "Pay", "lang": "en"})
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is not None
    assert body["error"] is None


@pytest.mark.asyncio
async def test_get_message_uk(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.post("/api/message/get",
                                 json={"message": "Оплата доставка", "lang": "uk"})
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is not None
    assert body["error"] is None


@pytest.mark.asyncio
async def test_get_message_ru(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.post("/api/message/get",
                                 json={"message": "Оплата доставка", "lang": "ru"})
    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["success"] is True
    assert body["data"] is not None
    assert body["error"] is None


@pytest.mark.asyncio
async def test_get_message_fail(client: AsyncClient):
    """
    Test cases for create_demo_database.
    :param client:
    :return:
    """
    response = await client.post("/api/message/get",
                                 json={"message": "Оплата доставка", "lang": "we"})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    body = response.json()
    assert body["success"] is False
    assert body["data"] is None
    assert body["error"] == "Lang not supported"


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
