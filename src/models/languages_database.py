"""
Languages Database
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.database import Language, session


class LanguagesDatabase:
    """
    Languages Database
    """

    def __init__(self):
        self.session = session

    def create(self, name: str) -> bool:
        """
        Create a new language
        :param name:
        :return:
        """
        try:
            name = escape(name)
            obj = Language(name=name)
            self.session.add(obj)
            self.session.commit()
            return True
        except IntegrityError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def update(self, idx: int, name: str) -> bool:
        """
        Update a language
        :param idx:
        :param name:
        :return:
        """
        try:
            query = select(Language).where(Language.id == idx)
            obj = self.session.execute(query)
            obj = obj.scalar_one_or_none()
            if obj is None:
                return False
            obj.name = name
            self.session.commit()
            return True
        except IntegrityError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def delete(self, idx: int) -> bool:
        """
        Delete a language
        :param idx:
        :return:
        """
        try:
            query = select(Language).where(Language.id == idx)
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
        Get a language
        :param idx:
        :return:
        """
        try:
            query = select(Language).where(Language.id == idx)
            obj = self.session.execute(query)
            result = obj.scalar_one_or_none()
            if result is None:
                return None
            return {
                'id': idx,
                'name': result.name
            }
        except ValueError as e:
            logging.error(e)
            return None

    def get_all(self) -> list[dict] | None:
        """
        Get all languages
        :return:
        """
        try:
            query = select(Language)
            obj = self.session.execute(query)
            result = obj.scalars().all()
            if result is None:
                return None
            return [{
                'id': p.id,
                'name': p.name
            } for p in result]
        except ValueError as e:
            logging.error(e)
            return None
