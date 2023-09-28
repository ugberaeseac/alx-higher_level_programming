#!/usr/bin/python3
"""
connects to a MySQL server running on localhost at port 3306
takes 4 arguments: mysql username, password, dbname and state name to search
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
    cursor.execute("SELECT * FROM `states`\
                   WHERE `name`=(%s) ORDER BY `id` ASC", (argv[4]))
    queryRows = cursor.fetchall()

    for rows in queryRows:
        print(rows)
    cursor.close()
    dBase.close()
