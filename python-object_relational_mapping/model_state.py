#!/usr/bin/python3
"""Define the State model mapped to the states table using SQLAlchemy ORM."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class mapped to the states table."""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
