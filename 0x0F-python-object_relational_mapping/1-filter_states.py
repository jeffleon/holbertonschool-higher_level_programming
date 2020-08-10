#!/usr/bin/python3
""" main function"""
if __name__ == '__main__':
    """ conect a db and query to elements that begin with letter N"""
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select * from states where name like 'N%' order by id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
