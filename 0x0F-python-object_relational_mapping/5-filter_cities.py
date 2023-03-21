#!/usr/bin/python3
'''A script that filters records from a named database'''

import MySQLdb
import sys


if __name__ == '__main__':
    username, password, database, name = sys.argv[1:5]

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
            SELECT cities.name
                FROM `cities`
                LEFT JOIN `states`
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state)s
                ORDER BY 'id'
            """, {'state': name}
        )
        rows = [row[0] for row in cur.fetchall()]
        print(', '.join(rows))
    db.close()
