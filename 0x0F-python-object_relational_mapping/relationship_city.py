#!/usr/bin/python3
'''A Model class for City'''

from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    '''A class modelling a city
    Attributes
    ----------
    id(int) - primary key
    name(str) - name of city
    state_id(int) - foreign key to state
    '''

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
        ForeignKey('states.id', ondelete='CASCADE'),
        nullable=False
    )

    state = relationship('State', )

    def __repr__(self) -> str:
        return f'<City(id={self.id} name={self.name} \
            state_id={self.state_id})>'
