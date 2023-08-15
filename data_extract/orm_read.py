def get_instance(db, model, skip: int = 0, limit: int = 100):
    instance = db.query(model).offset(skip).limit(limit).all()
    return instance
