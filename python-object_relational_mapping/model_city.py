#!/usr/bin/python3
"""
Define the City class mapped to the 'cities' table using SQLAlchemy ORM.

The City model includes an id primary key, a name field, and a state_id
foreign key that references states.id.
"""

from sqlalchemy import Column, Integer, String
from model_state import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=True)
