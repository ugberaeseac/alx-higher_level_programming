#!/usr/bin/python3
"""
Module: 4-cities_by_state
script that lists all cities from the database hbtn_0e_4_usa
connects to a MySQL server running on localhost at port 3306
takes 3 arguments: mysql username, password and databasename
can only use execute() once
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
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC;")
    queryRows = cursor.fetchall()

    for rows in queryRows:
        print(rows)
    cursor.close()
    dBase.close()
