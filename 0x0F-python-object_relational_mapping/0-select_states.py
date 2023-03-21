#!/usr/bin/python3

'''A script that lists all the states from
the database hbtn_0e_0_usa
'''

import sys
import MySQLdb

def run_script(username, password, database):
    '''runs a given SQL script using parameters'''
    db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit()
    username, password, database = sys.argv[1:4]
    run_script(username, password, database)
