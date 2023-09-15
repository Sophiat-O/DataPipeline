from .data_connection import get_session

Session = get_session()
session = Session()


def create_instance(model, kwargs, db=session):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance is None:
        add_instance = db.add(model(**kwargs))
        db.commit()
    return "Adding Instance To The Database"
