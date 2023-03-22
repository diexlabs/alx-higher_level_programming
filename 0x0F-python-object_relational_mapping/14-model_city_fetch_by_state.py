#!/usr/bin/python3
'''lists all city from the database'''

import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user, passwd, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db
    ))
    Base.metadata.create_all(engine)
    sess = sessionmaker(bind=engine)()

    cities = sess.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')
