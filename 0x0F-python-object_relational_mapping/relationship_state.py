#!/usr/bin/python3
'''A Model klas using sqlalcemy'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''A model klas for State'''
    __tablename__ = 'states'

    id = Column(
        Integer,
        Sequence('state_id_seq'),
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)

    cities = relationship('City', order_by='City.id', back_populates='state')