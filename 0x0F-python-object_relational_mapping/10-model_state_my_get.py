#!/usr/bin/python3

"""
prints the State object with the search name passed as argument
takes 3 arguments: username, password and dbname and state to search
imports State and Base from model_state
connects to a MySQL server running on localhost at port 3306
results sorted in ascending order by states.id
print Not found if no state was found else print id
"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    dbName = argv[3]
    searchState = argv[4]

    conn = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(conn.format(user, passwd, dbName))
    Session = sessionmaker(bind=engine)
    session = Session()

    queryData = session.query(State).filter_by(name=searchState).first()
    if queryData:
        print("{}".format(queryData.id))
    else:
        print("Not found")
