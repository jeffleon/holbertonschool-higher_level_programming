#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).filter(State.name.like("%a%"))
    for result in query:
        print("{} : {}".format(result.id, result.name))
        session.delete(result)
    session.commit()
    session.close()
