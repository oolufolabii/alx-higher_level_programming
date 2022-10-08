#!/usr/bin/python3
'''
Script that prints the first State object from the database hbtn_0e_6_usa
'''

from model_state import Base


if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')

    session.close()
