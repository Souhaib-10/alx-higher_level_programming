#!/usr/bin/python3
'''
    python file that contains the class definition of a State
    and instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    ''' Represents a state for a MySQL database.

    __tablename__(str): the name of mysql table
    id (sqlalchemy.Integer): The state's id.
    name ((sqlalchemy.String): The state's name.)
    '''
    __table__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(140), nullable=False)
