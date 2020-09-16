#!/usr/bin/python3
""" main function """
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    """ database """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    if query is not None:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
    session.close()
