#!/usr/bin/python3
"""
Module: 1-filter_states
script that lists all states with name starting with
uppercase "N" from the database hbtn_0e_0_usa
connects to a MySQL server running on localhost at port 3306
takes 3 arguments: mysql username, password and databasename
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
    cursor.execute("SELECT * FROM states WHERE `name`LIKE 'N%'\
                    ORDER BY `id` ASC;")
    queryRows = cursor.fetchall()

    for rows in queryRows:
        if (rows[1][0] == 'N'):
            print(rows)
    cursor.close()
    dBase.close()
