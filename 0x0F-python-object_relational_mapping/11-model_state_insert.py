#!/usr/bin/python3
"""
task 7 answer
"""


if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    user = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(
        State(name='Louisiana')
    )
    Base.metadata.create_all(engine)
    states = session.query(State).filter(
        State.name == 'Louisiana').order_by(State.id).all()
    if not states:
        print("Not found")
    for state in states:
        print(state.id)
    session.close()
