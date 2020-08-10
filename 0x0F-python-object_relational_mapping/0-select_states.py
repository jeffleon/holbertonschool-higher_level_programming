#!/usr/bin/python3
""" select all rows """
if __name__ == '__main__':
    import MySQLdb
    import sys
    """ Arguments """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states")
    rows = cursor.fetchall()
    for row in rows:
        print("{}".format(row))
    cursor.close()
    db.close()
