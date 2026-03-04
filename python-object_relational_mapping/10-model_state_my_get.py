#!/usr/bin/python3
"""Print the id of the State with the given name using SQLAlchemy."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        username, password, database
    )

    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
    )

    if st:
        print(st.id)
    else:
        print("Not found")

    session.close()
