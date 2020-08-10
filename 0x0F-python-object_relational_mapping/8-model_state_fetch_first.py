#!/usr/bin/python3
""" main function """
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    """ database """
    value = "mysql+mysqldb://{}:{}@localhost/{}"\
                           "".format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]), pool_pre_ping=True)
    engine = create_engine(value , pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()
    print("{} : {}".format(query.id, query.name))
    session.close()
