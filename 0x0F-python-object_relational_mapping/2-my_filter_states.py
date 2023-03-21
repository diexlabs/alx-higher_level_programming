#!/usr/bin/python3
'''A script that filters records from a named database'''

import MySQLdb
import sys


def run_script(username, password, database, name):
    '''connects to a database and prints filtered records'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY 'id'", (name,))
        for row in cur.fetchall():
            print(row)
    db.close()


if __name__ == '__main__':
    username, password, database, name = sys.argv[1:5]
    run_script(username, password, database, name)
