from . import models
from data_app.exception_handler import UnicornException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from data_app.orm_read import get_instance
from data_app.data_connection import get_session
from fastapi import Depends, FastAPI, HTTPException, Request

app = FastAPI()


# Dependency
def get_db():
    Session = get_session()
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! No data returned"},
    )


@app.get("/companies/")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = get_instance(db, models.Company, skip=skip, limit=limit)
    if companies is None:
        raise UnicornException()
    return companies
