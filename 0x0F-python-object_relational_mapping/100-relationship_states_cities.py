#!/usr/bin/python3
'''
Script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
'''

if __name__ == '__main__':
    
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    
    session = Session(engine)
    
    new_city_name = City(name='San Francisco')
    
    new_state_name = State(name='California')
    new_state_name.cities.append(new_city_name)
    
    session.add_all([new, new_city_name])
    
    session.commit()
    
    session.close()
