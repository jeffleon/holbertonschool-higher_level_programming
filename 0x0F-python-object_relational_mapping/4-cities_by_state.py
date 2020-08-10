#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("select cities.id, cities.name, states.name "
               "from cities inner join states "
               "on cities.state_id = states.id "
               "order by cities.id ASC;")
results = cursor.fetchall()
for result in results:
    print(result)
cursor.close()
db.close()
