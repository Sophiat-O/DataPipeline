def create_instance(db, model):
    add_instance = db.add(model)
    db.commit()
    return add_instance
