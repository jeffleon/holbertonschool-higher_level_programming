#!/usr/bin/python3
""" function main """
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import Base, City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine, join
    """ main """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    for states, cities in session.query(State, City)\
                                 .filter(City.state_id == State.id)\
                                 .order_by(City.id)\
                                 .all():
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
