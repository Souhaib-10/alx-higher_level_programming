#!/usr/bin/python3
'''
    script lists all state by use ORM
'''


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connection_string = "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connection_string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
