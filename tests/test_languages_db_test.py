"""
Test suite for test_languages.
"""
import pytest

from src.models.languages_database import LanguagesDatabase


@pytest.mark.parametrize("name", ["en", "ru", "uk"])
def test_languages_create(name):
    """
    Test creating a language.
    :param name:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.create(name)
    assert result is True


@pytest.mark.parametrize("name", ["en", "ru", "uk"])
def test_languages_create_false(name):
    """
    Test creating a language.
    :param name:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.create(name)
    assert result is False


@pytest.mark.parametrize("idx, name", [(1, "en"), (2, "ru"), (3, "uk")])
def test_languages_get_one(idx, name):
    """
    Test getting one language.
    :param idx:
    :param name:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.get_one(idx=idx)
    assert result['name'] == name


@pytest.mark.parametrize("idx, name", [(1, "english"), (2, "russian"), (3, "ukraine")])
def test_languages_update(idx, name):
    """
    Test updating a language.
    :param idx:
    :param name:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.update(idx=idx, name=name)
    assert result is True


@pytest.mark.parametrize("idx, name", [(2, "english"), (3, "english")])
def test_languages_update_false(idx, name):
    """
    Test updating a language.
    :param idx:
    :param name:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.update(idx=idx, name=name)
    assert result is False


def test_languages_get_all():
    """
    Test getting all languages.
    :return:
    """
    obj = LanguagesDatabase()
    results = obj.get_all()
    for result in results:
        assert result['name'] in ["english", "russian", "ukraine"]
        assert result['id'] in [1, 2, 3]


@pytest.mark.parametrize("idx", [1, 2, 3])
def test_languages_delete(idx):
    """
    Test deleting a language.
    :param idx:
    :return:
    """
    obj = LanguagesDatabase()
    result = obj.delete(idx=idx)
    assert result is True
