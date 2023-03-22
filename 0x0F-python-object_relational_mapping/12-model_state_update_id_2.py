#!/usr/bin/python3
'''updates a State record in the database'''


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

    state = sess.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    sess.commit()
