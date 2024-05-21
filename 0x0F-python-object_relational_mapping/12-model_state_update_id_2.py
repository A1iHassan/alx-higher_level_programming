#!/usr/bin/python3
"""
task 12 answer
"""


if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import State, Base
    from sys import argv

    user = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}')
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    try:
        state_to_change = session.query(
            State).filter(State.id == 2).one_or_none()
        if state_to_change:
            state_to_change.name = 'New Mexico'
            session.commit()
    except Exception as e:
        session.rollback()
    finally:
        session.close()
