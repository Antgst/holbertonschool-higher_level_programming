#!/usr/bin/python3
"""Print the first State object from the database using SQLAlchemy."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        username, password, database
    )

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
