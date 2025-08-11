"""
Question Database
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.database import Question, session, Language, Category


class QuestionsDatabase:
    """
    Question Database
    """

    def __init__(self):
        self.session = session

    def create(self, name: str, category_id: int, language_id: int) -> bool:
        """
        Create a new question
        :param language_id:
        :param category_id:
        :param name:
        :return:
        """
        try:
            name = escape(name)
            obj = Question(
                name=name,
                category_id=category_id,
                language_id=language_id
            )
            self.session.add(obj)
            self.session.commit()
            return True
        except IntegrityError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def update(self,
               idx: int,
               name: str,
               category_id: int,
               language_id: int
               ) -> bool:
        """
        Update a question
        :param language_id:
        :param category_id:
        :param idx:
        :param name:
        :return:
        """
        try:
            query = select(Question).where(Question.id == idx)
            obj = self.session.execute(query)
            obj = obj.scalar_one_or_none()
            if obj is None:
                return False
            obj.name = name
            obj.category_id = category_id
            obj.language_id = language_id
            self.session.commit()
            return True
        except IntegrityError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def delete(self, idx: int) -> bool:
        """
        Delete a question
        :param idx:
        :return:
        """
        try:
            query = select(Question).where(Question.id == idx)
            obj = self.session.execute(query)
            result = obj.scalar_one_or_none()
            self.session.delete(result)
            self.session.commit()
            return True
        except ValueError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def get_one(self, idx: int) -> dict | None:
        """
        Get a question
        :param idx:
        :return:
        """
        try:
            query = (
                select(Question.id,
                       Question.name.label("name"),
                       Language.name.label("language"),
                       Language.id.label("language_id"),
                       Category.name.label("category"),
                       Category.id.label("category_id"),
                       )
                .join(Language, Language.id == Question.language_id)
                .join(Category, Category.id == Question.category_id)
                .where(Question.id == idx))
            obj = self.session.execute(query)
            result = obj.one()
            if result is None:
                return None
            return {
                'id': idx,
                'name': result.name,
                'language': result.language,
                'language_id': result.language_id,
                'category': result.category,
                'category_id': result.category_id
            }
        except ValueError as e:
            logging.error(e)
            return None

    def get_all(self) -> list[dict] | None:
        """
        Get all questions
        :return:
        """
        try:
            query = (
                select(Question.id.label("id"),
                       Question.name.label("name"),
                       Language.name.label("language"),
                       Language.id.label("language_id"),
                       Category.name.label("category"),
                       Category.id.label("category_id"),
                       )
                .join(Language, Language.id == Question.language_id)
                .join(Category, Category.id == Question.category_id)
            )
            obj = self.session.execute(query)
            result = obj.all()
            if result is None:
                return None
            return [{
                'id': p.id,
                'name': p.name,
                'language': p.language,
                'language_id': p.language_id,
                'category': p.category,
                'category_id': p.category_id
            } for p in result]
        except ValueError as e:
            logging.error(e)
            return None
