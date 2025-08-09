"""
Test suite for test_questions.
"""
import pytest

from src.models.questions_database import QuestionsDatabase
from src.models.categories_database import CategoriesDatabase
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


@pytest.mark.parametrize("name, languages_id, categories_id", [
    ("Some text 1 1", 1, 1), ("Some text 2 1", 2, 1), ("Some text 3 1", 3, 1),
    ("Some text 1 2", 1, 2), ("Some text 2 2", 2, 2), ("Some text 3 2", 3, 2),
    ("Some text 1 3", 1, 3), ("Some text 2 3", 2, 3), ("Some text 3 3", 3, 3)
])
def test_question_create(name, languages_id, categories_id):
    """
    Test creating a question.
    :param name:
    :return:
    """
    obj = QuestionsDatabase()
    result = obj.create(name=name, language_id=languages_id, category_id=categories_id)
    assert result is True


@pytest.mark.parametrize("idx, name", [
    (1, "Some text 1 1"), (2, "Some text 2 1"), (3, "Some text 3 1"),
    (4, "Some text 1 2"), (5, "Some text 2 2"), (6, "Some text 3 2"),
    (7, "Some text 1 3"), (8, "Some text 2 3"), (9, "Some text 3 3")
])
def test_question_get_one(idx, name):
    """
    Test getting one question.
    :param idx:
    :param name:
    :return:
    """
    obj = QuestionsDatabase()
    result = obj.get_one(idx=idx)
    assert result['name'] == name


@pytest.mark.parametrize("idx, name, categories_id, languages_id", [
    (1, "Some text 1 1 0", 1, 1), (2, "Some text 2 1 0", 2, 1), (3, "Some text 3 1 0", 3, 1),
    (4, "Some text 1 2 0", 1, 2), (5, "Some text 2 2 0", 2, 2), (6, "Some text 3 2 0", 3, 2),
    (7, "Some text 1 3 0", 1, 3), (8, "Some text 2 3 0", 2, 3), (9, "Some text 3 3 0", 3, 3)
])
def test_question_update(idx, name, categories_id, languages_id):
    """
    Test updating a question.
    :param idx:
    :param name:
    :return:
    """
    obj = QuestionsDatabase()
    result = obj.update(idx=idx, name=name, category_id=categories_id, language_id=languages_id)
    assert result is True


def test_questions_get_all():
    """
    Test getting all questions.
    :return:
    """
    obj = QuestionsDatabase()
    results = obj.get_all()
    list_questions = [
        "Some text 1 1 0", "Some text 2 1 0", "Some text 3 1 0",
        "Some text 1 2 0", "Some text 2 2 0", "Some text 3 2 0",
        "Some text 1 3 0", "Some text 2 3 0", "Some text 3 3 0"
    ]
    for result in results:
        assert result['name'] in list_questions
        assert result['id'] in [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize("idx", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_questions_delete(idx):
    """
    Test deleting questions.
    :param idx:
    :return:
    """
    obj = QuestionsDatabase()
    result = obj.delete(idx=idx)
    assert result is True


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
