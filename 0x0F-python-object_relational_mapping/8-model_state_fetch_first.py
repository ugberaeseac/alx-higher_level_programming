#!/usr/bin/python3

"""
list the first State objects from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
imports State and Base from model_state
connects to a MySQL server running on localhost at port 3306
results sorted in ascending order by states.id
print Nothing if the table is empty
"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    dbName = argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(conn.format(user, passwd, dbName))
    Session = sessionmaker(bind=engine)
    session = Session()

    queryData = session.query(State).order_by(State.id).first()
    if queryData:
            print("{}: {}".format(queryData.id, queryData.name))
    else:
            print("Nothing")

