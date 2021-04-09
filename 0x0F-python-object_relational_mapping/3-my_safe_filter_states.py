#!/usr/bin/python3
'''python-ORM'''
import sys
import MySQLdb

if __name__ == '__main__':
    u_name = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host='localhost', port=3306, user=u_name,
                                passwd=passwd, db=db_name, charset='utf8')

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(name)s\
    ORDER BY id ASC", {'name': state_name})
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
