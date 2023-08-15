from sqlalchemy.orm import Session


def get_instance(db, model):
    instance = db.query(model).all()
    return instance
