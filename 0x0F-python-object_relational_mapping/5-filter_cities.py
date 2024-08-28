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
    cur.execute("SELECT c.name \
                    FROM cities as c, states as s \
                    WHERE c.state_id =  s.id \
                    and s.name = %s \
                    ORDER BY c.id", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
