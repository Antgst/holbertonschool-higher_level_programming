#!/usr/bin/python3
"""
Update the name of the State with id 2 in the hbtn_0e_6_usa database
to 'New Mexico' using SQLAlchemy.
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

    state = session.get(State, 2)
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()
