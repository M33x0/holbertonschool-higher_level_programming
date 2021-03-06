#!/usr/bin/python3
'''python-ORM: List cities by states,ascending order by cities.id'''
import sys
import MySQLdb

if __name__ == '__main__':
    u_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(host='localhost', port=3306, user=u_name,
                                passwd=passwd, db=db_name, charset='utf8')

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM states \
    JOIN cities WHERE cities.state_id = states.id ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
