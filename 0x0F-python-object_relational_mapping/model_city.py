#!/usr/bin/python3
"""
task 14 answer
"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class City(Base):
    """
    a class that maps to the cities table

    Attributes:
        id: class attribute
        name: class attribute
    """

    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
