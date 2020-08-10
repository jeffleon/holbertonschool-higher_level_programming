#!/usr/bin/python3
""" main function """
if __name__ == '__main__':
    import MySQLdb
    import sys
    """ find a coincidence between database and typed arg"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "select * from states where name like binary '{}'"\
        .format(sys.argv[4])
    cursor.execute(query)
    results = cursor.fetchall()
    for result in results:
        print(result)
    cursor.close()
    db.close()
