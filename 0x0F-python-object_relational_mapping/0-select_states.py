#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("select * from states")
rows = cursor.fetchall()
for row in rows:
    print("{}".format(row))
db.close()
