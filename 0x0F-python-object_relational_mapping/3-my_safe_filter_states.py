#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
query = "select * from states where name = %s;"
cursor.execute(query, (sys.argv[4],))
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()
db.close()
