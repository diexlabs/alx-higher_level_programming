#!/usr/bin/python3
'''A Model klas using sqlalcemy'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(
        Integer,
        Sequence('state_id_seq'),
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
