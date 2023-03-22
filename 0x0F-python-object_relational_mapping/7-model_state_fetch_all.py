#!/usr/bin/python3
'''filter states records from database
order records by id
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(username, password, database),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()
    states = sess.query(State).order_by(State.id)
    for state in states:
        print(f'{state.id}: {state.name}')
