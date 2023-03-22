#!/usr/bin/python3
'''filters all states record containing a in name'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    user, passwd, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db
    ))
    Base.metadata.create_all(engine)

    sess = sessionmaker(bind=engine)()
    states = sess.query(State).filter(
        State.name.contains('a')
        ).order_by(State.id)

    for state in states:
        print(f'{state.id}: {state.name}')
