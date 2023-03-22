#!/usr/bin/python3
'''filters all states record that have given name'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    user, passwd, db, name = sys.argv[1:5]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db
    ))
    Base.metadata.create_all(engine)

    sess = sessionmaker(bind=engine)()
    state = sess.query(State).filter(
        State.name == name
        ).order_by(State.id).first()

    if not state:
        print('Not found')
    else:
        print(f'{state.id}')
