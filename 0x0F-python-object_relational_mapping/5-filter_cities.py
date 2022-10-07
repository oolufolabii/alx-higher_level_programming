#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 5:

        db_connection = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3])

        cur = db_connection.cursor()
        state_input = sys.argv[4]
        cur.execute('SELECT cities.name FROM cities INNER JOIN'
                    'states ON cities.state_id = states.id'
                    'WHERE BINARY states.name=%s'
                    'ORDER BY cities.id ASC;', [state_input]
                    )

        row_result = cur.fetchall()
        print(", ".join([row[0] for row in row_result]))

        db_connection.close()
