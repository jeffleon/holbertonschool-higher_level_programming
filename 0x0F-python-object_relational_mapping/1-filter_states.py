#!/usr/bin/python3
import MySQLdb
import sys
""" main function"""
if __name__ == '__main__':
    """ conect a db and query to elements that begin with letter N"""
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states where name like 'N%'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
