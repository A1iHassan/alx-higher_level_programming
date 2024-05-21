#!/usr/bin/python3
"""
task 14 answer
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv

    user = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}city.state.) {city.name}")
    session.close()
