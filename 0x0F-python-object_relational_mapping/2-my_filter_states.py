#!/usr/bin/python3
"""
Module: 2-my_filter_states

script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
connects to a MySQL server running on localhost at port 3306
takes 4 arguments: mysql username, password database and name to search
uses "format" to create the SQL query with the user input
results sorted in ascending order by state id
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    dBase = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=argv[1],
                            passwd=argv[2],
                            db=argv[3])
    cursor = dBase.cursor()
    cursor.execute("""SELECT *
                   FROM states
                   WHERE name='{:s}'
                   ORDER BY states.id ASC""".format(argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        if (row[1] == argv[4]):
            print(row)

    cursor.close()
    dBase.close()
