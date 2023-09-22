#!/usr/bin/python3
"""
Module: 5-filter_cities
takes in the name of a state as argument and
lists all cities from the database hbtn_0e_4_usa
connects to a MySQL server running on localhost at port 3306
takes 4 arguments: mysql username, password and databasename and name of state
can only use execute() once
results sorted in ascending order by cities.id
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
    cursor.execute("SELECT cities.name\
                    FROM `cities`\
                    JOIN `states` ON state_id=states.id\
                    WHERE states.name=(%s)\
                    ORDER BY cities.id", argv[4])
    queryRows = cursor.fetchall()

    for rows in queryRows:
        print(rows, end=",")
    cursor.close()
    dBase.close()
