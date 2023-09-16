#!/usr/bin/python3
"""
This script defines a City class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the city
        id (int): The City id of the class
        name (str): The City name of the class

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    states_id =Column(Integer, ForeignKey('states.id'), nullable=False)
