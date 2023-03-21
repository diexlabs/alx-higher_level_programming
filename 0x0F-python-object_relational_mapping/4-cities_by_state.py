#!/usr/bin/python3
'''A script that filters records from a named database'''

import MySQLdb
import sys


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    with db.cursor() as cur:
        cur.execute(
            """
            SELECT city.id, city.name, state.name
            FROM `cities` AS city
            LEFT JOIN states AS state
            ON city.state_id = state.id
            ORDER BY city.id ASC
            """
        )
        for row in cur.fetchall():
            print(row)
    db.close()
