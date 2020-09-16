#!/usr/bin/python3
""" function main """
if __name__ == '__main__':
    import MySQLdb
    import sys
    """ database """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("select cities.name "
                   "from cities inner join states "
                   "on cities.state_id = states.id "
                   "where states.name = %s "
                   "order by cities.id ASC;", (sys.argv[4],))
    result = list()
    results = cursor.fetchall()
    for tuple_ in results:
        if tuple_[0] not in result:
            result.append(tuple_[0])
    print(", ".join(result))
    cursor.close()
    db.close()
