#!/usr/bin/python3

'''
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
        cur.execute("SELECT * FROM states WHERE BINARY name like BINARY {}"
                    "ORDER BY states.id ASC;".format(sys.argv[4]))

        row_result = cur.fetchall()
        for row in row_result:
            print(row)

        db_connection.close()
