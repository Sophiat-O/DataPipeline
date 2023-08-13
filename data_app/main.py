from . import models
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException


from data_app.orm_read import get_instance
from data_app.data_connection import get_session

app = FastAPI()


# Dependency
def get_db():
    Session = get_session()
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/companies")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = get_instance(db, models.Company, skip=skip, limit=limit)
    if companies is None:
        raise HTTPException(status_code=404, detail="No data found")
    return companies


@app.get("/markets")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    markets = get_instance(db, models.Market, skip=skip, limit=limit)
    if markets is None:
        raise HTTPException(status_code=404, detail="No data found")
    return markets


@app.get("/geography")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    location = get_instance(db, models.Geography, skip=skip, limit=limit)
    if location is None:
        raise HTTPException(status_code=404, detail="No data found")
    return location


@app.get("/company_stock")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    company_stock = get_instance(db, models.CompanyStock, skip=skip, limit=limit)
    if company_stock is None:
        raise HTTPException(status_code=404, detail="No data found")
    return company_stock


@app.get("/market_index")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    market_index = get_instance(db, models.MarketIndex, skip=skip, limit=limit)
    if market_index is None:
        raise HTTPException(status_code=404, detail="No data found")
    return market_index


@app.get("/index_stock")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    index_stock = get_instance(db, models.IndexStock, skip=skip, limit=limit)
    if index_stock is None:
        raise HTTPException(status_code=404, detail="No data found")
    return index_stock


@app.get("/gics")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    gics_class = get_instance(db, models.GICSClassification, skip=skip, limit=limit)
    if gics_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return gics_class


@app.get("/naics")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    naics_class = get_instance(db, models.NAICSClassification, skip=skip, limit=limit)
    if naics_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return naics_class


@app.get("/trbc/")
def get_companies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trbc_class = get_instance(db, models.TRBCClassification, skip=skip, limit=limit)
    if trbc_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return trbc_class
