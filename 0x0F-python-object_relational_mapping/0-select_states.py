#!/usr/bin/python3
import MySQLdb
import sys
""" select all rows """
if __name__ == '__main__':
    """ Arguments """
    db = MySQLdb.connect(host="127.0.0.1",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states")
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
    cursor.close()
    db.close()
