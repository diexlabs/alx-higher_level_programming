#!/usr/bin/python3
'''list all cities alongside their state'''

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

    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')
