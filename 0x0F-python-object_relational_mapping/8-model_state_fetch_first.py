#!/usr/bin/python3
'''filters the first state record from database'''

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database
    ))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()

    state = sess.query(State).order_by(State.id).first()
    if not state:
        print('Nothing')
    else:
        print(f'{state.id}: {state.name}')
