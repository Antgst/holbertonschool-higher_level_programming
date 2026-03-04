#!/usr/bin/python3
"""List all states from the database whose name starts with N."""

import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, name "
        "FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
