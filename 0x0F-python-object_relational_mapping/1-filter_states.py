#!/usr/bin/python3
""" This module connet to a database"""


if __name__ == "__main_":
    import MySQLdb
    import sys

    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )

    db_cursor = db_connection.cursor()
    db_cursor.execute(
            """SELECT * FROM states WHERE name LIKE
            BINARY 'N%' ORDER BY states.id ASC
            """
            )

    for row in db_cursor.fetchall():
        print(row)

    db_cursor.close()
    db_connection.close()
