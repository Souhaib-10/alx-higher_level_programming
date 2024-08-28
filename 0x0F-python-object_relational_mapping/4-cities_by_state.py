#!/usr/bin/python3
'''
    list all cities from hbtn_0e_4_usa
'''

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                    FROM cities as c, states as s \
                    WHERE c.state_id =  s.id \
                    ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
