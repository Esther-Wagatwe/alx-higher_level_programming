#!/usr/bin/python3
"""deletes all State objects with a name containing letter a from the db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    for i in delete_state:
        session.delete(i)

    session.commit()
    session.close()
