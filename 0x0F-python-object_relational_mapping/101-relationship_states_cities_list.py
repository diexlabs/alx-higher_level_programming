#!/usr/bin/python3
'''list all states and corresponding cities'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == '__main__':
    user, passwd, db = sys.argv[1:4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(user, passwd, db)
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    states = session.query(State).order_by(State.id)
    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')
