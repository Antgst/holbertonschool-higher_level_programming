#!/usr/bin/python3
"""List all cities of a given state from the database,
safely and ordered by cities.id."""

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
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state,))

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()

    db.close()
