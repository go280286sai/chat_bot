"""
Database for chat work. Contains languages, questions, and answers.
"""
# pylint: disable=too-few-public-methods
from datetime import datetime

from sqlalchemy import Integer, Column, String, create_engine, DateTime, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///database.db')


class Base(DeclarativeBase):
    pass


class Language(Base):
    """
    Contains languages.
    """
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Category(Base):
    """
    Contains categories.
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Question(Base):
    """
    Contains questions.
    """
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    language_id = Column(Integer, ForeignKey('languages.id', ondelete='CASCADE'))
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.utcnow)


class Answer(Base):
    """
    Contains answers.
    """
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))
    language_id = Column(Integer, ForeignKey('languages.id', ondelete='CASCADE'))
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
