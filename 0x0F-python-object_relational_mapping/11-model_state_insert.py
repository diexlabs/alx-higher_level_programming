#!/usr/bin/python3
'''adds a new State record to database'''


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

if __name__ == '__main__':
    user, passwd, db = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, passwd, db
    ))
    Base.metadata.create_all(engine)
    sess = sessionmaker(bind=engine)()

    state = State(name='Louisiana')
    sess.add(state)
    new = sess.query(State).filter(State.name == 'Louisiana').first()
    print(new.id)
    sess.commit()
