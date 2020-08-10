#!/usr/bin/python3
""" function main"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    """ main """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    myobject = State(name='Louisiana')
    session.add(myobject)
    session.commit()
    print(myobject.id)
    session.close()
