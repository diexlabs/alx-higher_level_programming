#!/usr/bin/python3
'''A script that filters records from a named database'''

import MySQLdb
import sys


def run_script(username, password, database):
    '''connects to a database and prints filtered records'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute(
        """
        SELECT *
            FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY 'id'
        """
    )
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    username, password, database = sys.argv[1:4]
    run_script(username, password, database)
