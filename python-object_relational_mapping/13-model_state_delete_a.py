#!/usr/bin/python3
"""
Delete all State objects from the hbtn_0e_6_usa database whose name
contains the letter 'a' using SQLAlchemy.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database
    )

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like("%a%")).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
