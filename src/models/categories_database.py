"""
Categories Database
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.database import Category, session


class CategoriesDatabase:
    """
    Categories Database
    """
    def __init__(self):
        self.session = session

    def create(self, name: str) -> bool:
        """
        Create a new categories
        :param name:
        :return:
        """
        try:
            name = escape(name)
            obj = Category(name=name)
            self.session.add(obj)
            self.session.commit()
            return True
        except IntegrityError as e:
            logging.error(e)
            self.session.rollback()
            return False

    def update(self, idx: int, name: str) -> bool:
        """
        Update a categories
        :param idx:
        :param name:
        :return:
        """
        try:
            query = select(Category).where(Category.id == idx)
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
        Delete a categories
        :param idx:
        :return:
        """
        try:
            query = select(Category).where(Category.id == idx)
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
        Get a categories
        :param idx:
        :return:
        """
        try:
            query = select(Category).where(Category.id == idx)
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
        Get all categories
        :return:
        """
        try:
            query = select(Category)
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
