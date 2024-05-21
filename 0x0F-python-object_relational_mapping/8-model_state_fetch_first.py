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
    Base.metadata.create_all(engine)
    state = session.query(State).order_by(State.id).first()
    if not state:
        print('Nothing')
    else:
        print(f"{state.id}: {state.name}")
    session.close()
