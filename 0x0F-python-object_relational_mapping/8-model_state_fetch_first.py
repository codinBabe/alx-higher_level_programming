#!/usr/bin/python3


"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    my_session = sessionmaker(bind=engine)
    session = my_session()

    first_state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(first_state.id, first_state.name))

    session.close()
