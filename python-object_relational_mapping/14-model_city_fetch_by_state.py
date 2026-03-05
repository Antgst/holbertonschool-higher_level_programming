#!/usr/bin/python3
"""
List all City objects from the database and display them with their State.

The script retrieves all cities ordered by cities.id and prints each line as:
<state name>: (<city id>) <city name>.
"""

import sys
from model_state import Base, State
from model_city import City
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

    rows = (
        session.query(State.name, City.id, City.name)
        .join(City, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    for state_name, city_id, city_name in rows:
        print("{}: ({}) {}".format(state_name, city_id, city_name))

    session.close()
