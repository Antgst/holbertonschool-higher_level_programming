#!/usr/bin/python3
"""List states from the database whose name matches the user input."""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    query = (
        "SELECT states.id, states.name "
        "FROM states "
        "WHERE name = BINARY '{}' "
        "ORDER BY states.id ASC"
    ).format(state)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()

    db.close()
