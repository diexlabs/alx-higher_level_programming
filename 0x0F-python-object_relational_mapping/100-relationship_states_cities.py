#!/usr/bin/python3
'''Create a state with a city'''

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

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.add(city)
    session.commit()
