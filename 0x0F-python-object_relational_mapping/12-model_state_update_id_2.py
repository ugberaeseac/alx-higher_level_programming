#!/usr/bin/python3

"""
update the name of a State object from the database hbtn_0e_6_usa
takes 3 arguments: username, password and dbname and state to search
imports State and Base from model_state
connects to a MySQL server running on localhost at port 3306i
update the name of the State where id = 2 to New Mexico
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

    queryData = session.query(State).filter_by(id=2).first()
    queryData.name = "New Mexico"
    session.commit()
