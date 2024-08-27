#!/usr/bin/python3
''' use ORM to connect a database with python code
    lists all states from the database hbtn_0e_0_usa
'''

import sys
import MySQLdb

if __name__ == "__main__":
    argu = sys.argv
    db = MySQLdb.connect(user=argu[1], password=argu[2], database=argu[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
