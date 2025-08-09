"""
Test suite for test_categories.
"""
import pytest

from src.models.categories_database import CategoriesDatabase


@pytest.mark.parametrize("name", ["General", "Delivery", "Pay"])
def test_categories_create(name):
    """
    Test creating a categories.
    :param name:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.create(name)
    assert result is True


@pytest.mark.parametrize("name", ["General", "Delivery", "Pay"])
def test_categories_create_fail(name):
    """
    Test creating a categories.
    :param name:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.create(name)
    assert result is False


@pytest.mark.parametrize("idx, name", [(1, "General"), (2, "Delivery"), (3, "Pay")])
def test_categories_get_one(idx, name):
    """
    Test getting one category.
    :param idx:
    :param name:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.get_one(idx=idx)
    assert result['name'] == name


@pytest.mark.parametrize("idx, name", [(1, "General_"), (2, "Delivery_"), (3, "Pay_")])
def test_categories_update(idx, name):
    """
    Test updating a category.
    :param idx:
    :param name:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.update(idx=idx, name=name)
    assert result is True


@pytest.mark.parametrize("idx, name", [(2, "General_"), (3, "General_")])
def test_categories_update_fail(idx, name):
    """
    Test updating a category.
    :param idx:
    :param name:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.update(idx=idx, name=name)
    assert result is False


def test_categories_get_all():
    """
    Test getting all categories.
    :return:
    """
    obj = CategoriesDatabase()
    results = obj.get_all()
    for result in results:
        assert result['name'] in ["General_", "Delivery_", "Pay_"]
        assert result['id'] in [1, 2, 3]


@pytest.mark.parametrize("idx", [1, 2, 3])
def test_categories_delete(idx):
    """
    Test deleting a categories.
    :param idx:
    :return:
    """
    obj = CategoriesDatabase()
    result = obj.delete(idx=idx)
    assert result is True
