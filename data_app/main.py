from . import models
from sqlalchemy.orm import Session
from data_app.orm_read import get_instance
from data_app.data_connection import get_session
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()


# Dependency
def get_db():
    Session = get_session()
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/companies/")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = get_instance(db, models.Company, skip=skip, limit=limit)
    if companies is None:
        raise HTTPException(status_code=404, detail="No data found")
    return companies
