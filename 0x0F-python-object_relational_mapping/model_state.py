#!/usr/bin/python3
"""
task 6 answer
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    a class that maps to the states table

    Attributes:
        id: class attribute
        name: class attribute
    """

    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128))
