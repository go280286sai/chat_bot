"""
Answers Database
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.database import Answer, session, Language, Category


class AnswersDatabase:
    """
    Answers Database
    """

    def __init__(self):
        self.session = session

    def create(self, name: str, category_id: int, language_id: int) -> bool:
        """
        Create a new answer
        :param language_id:
        :param category_id:
        :param name:
        :return:
        """
        try:
            name = escape(name)
            obj = Answer(
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
        Update answers
        :param language_id:
        :param category_id:
        :param idx:
        :param name:
        :return:
        """
        try:
            query = select(Answer).where(Answer.id == idx)
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
        Delete an answer
        :param idx:
        :return:
        """
        try:
            query = select(Answer).where(Answer.id == idx)
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
        Get an answer
        :param idx:
        :return:
        """
        try:
            query = (
                select(Answer.id,
                       Answer.name.label("name"),
                       Language.name.label("language"),
                       Category.name.label("category")
                       )
                .join(Language, Language.id == Answer.language_id)
                .join(Category, Category.id == Answer.category_id)
                .where(Answer.id == idx))
            obj = self.session.execute(query)
            result = obj.one()
            if result is None:
                return None
            return {
                'id': idx,
                'name': result.name,
                'language': result.language,
                'category': result.category
            }
        except ValueError as e:
            logging.error(e)
            return None

    def get_all(self) -> list[dict] | None:
        """
        Get all answers
        :return:
        """
        try:
            query = (
                select(Answer.id.label("id"),
                       Answer.name.label("name"),
                       Language.name.label("language"),
                       Category.name.label("category")
                       )
                .join(Language, Language.id == Answer.language_id)
                .join(Category, Category.id == Answer.category_id)
            )
            obj = self.session.execute(query)
            result = obj.all()
            if result is None:
                return None
            return [{
                'id': p.id,
                'name': p.name,
                'language': p.language,
                'category': p.category
            } for p in result]
        except ValueError as e:
            logging.error(e)
            return None
