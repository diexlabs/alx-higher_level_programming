#!/usr/bin/python3
'''A Model class for City'''

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    __tablename__ = 'cities'

    id = Column(
        Integer,
        Sequence('city_id_seq'),
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )

    state = relationship('State')

    def __repr__(self) -> str:
        return f'<City(id={self.id} name={self.name} \
            state_id={self.state_id})>'
