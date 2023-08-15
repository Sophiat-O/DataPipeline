from .data_connection import get_session

Session = get_session()
session = Session()


def create_instance(model, kwargs, db=session):
    add_instance = db.add(model(**kwargs))
    db.commit()
    return add_instance
