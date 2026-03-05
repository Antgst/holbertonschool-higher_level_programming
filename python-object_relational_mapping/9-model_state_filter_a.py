#!/usr/bin/python3
"""List all State objects that contain the letter 'a' using SQLAlchemy."""

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

    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    for st in states:
        print("{}: {}".format(st.id, st.name))

    session.close()
