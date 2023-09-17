#!/usr/bin/python3

"""
lists all State objects that contain the letter a from the database
takes 3 arguments: mysql username, mysql password and database name
imports State and Base from model_state
connects to a MySQL server running on localhost at port 3306
results sorted in ascending order by states.id
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    dbName = argv[3]

    conn = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(user, passwd, dbName))
    Session = sessionmaker(bind=engine)
    session = Session()

    queryData = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
    for data in queryData:
        print("{}: {}".format(data.id, data.name))
