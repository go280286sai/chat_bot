"""
Database for chat work. Contains languages, questions, and answers.
"""
# pylint: disable=too-few-public-methods
from datetime import datetime

from sqlalchemy import (Integer, Column, String,
                        create_engine, DateTime, ForeignKey, Text)
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

engine = create_engine('sqlite:///database.db')


# pylint: disable=unnecessary-pass
class Base(DeclarativeBase):
    """
    Base class for all models.
    """
    pass


class Language(Base):
    """
    Contains languages.
    """
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Category(Base):
    """
    Contains categories.
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class Question(Base):
    """
    Contains questions.
    """
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True)
    language_id = Column(Integer,
                         ForeignKey(
                             'languages.id',
                             ondelete='CASCADE')
                         )
    category_id = Column(Integer,
                         ForeignKey(
                             'categories.id',
                             ondelete='CASCADE')
                         )
    created_at = Column(DateTime, default=datetime.utcnow)


class Answer(Base):
    """
    Contains answers.
    """
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, unique=True)
    category_id: Mapped[int] = mapped_column(Integer,
                                             ForeignKey(
                                                 'categories.id',
                                                 ondelete='CASCADE')
                                             )
    language_id: Mapped[int] = mapped_column(Integer,
                                             ForeignKey(
                                                 'languages.id',
                                                 ondelete='CASCADE')
                                             )
    created_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, category_id: int, language_id: int, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.category_id = category_id
        self.language_id = language_id


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
