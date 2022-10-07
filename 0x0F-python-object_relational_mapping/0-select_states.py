#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa.
'''

if __name__ == '__main__':
    import MySQLdb
    import sys

    if len(sys.argv) >= 4:

        db_connection = MySQLdb.connect(host='localhost',
                                        port=3306,
                                        user=sys.argv[1],
                                        passwd=sys.argv[2],
                                        db=sys.argv[3])

        cur = db_connection.cursor()
        cur.execute('SELECT * FROM states ORDER BY id ASC;')

        row_result = cur.fetchall()
        for row in row_result:
            print(row)

        db_connection.close()
