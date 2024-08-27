#!/usr/bin/python3
''' use ORM to connect a database with python code
    lists all states with a name starting with N
'''

import sys
import MySQLdb

if __name__ == "__main__":
    argu = sys.argv
    db = MySQLdb.connect(user=argu[1], password=argu[2], database=argu[3])
    c = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
    query = query.format(argu[4])
    c.execute(query)
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
