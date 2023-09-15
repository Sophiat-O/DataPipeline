import models
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from orm_read import get_instance
from data_connection import get_session

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
def get_companies(db: Session = Depends(get_db)):
    companies = get_instance(db, models.Company)
    if companies is None:
        raise HTTPException(status_code=404, detail="No data found")
    return companies


@app.get("/markets")
def get_markets(db: Session = Depends(get_db)):
    markets = get_instance(db, models.Market)
    if markets is None:
        raise HTTPException(status_code=404, detail="No data found")
    return markets


@app.get("/geography")
def get_geography(db: Session = Depends(get_db)):
    location = get_instance(db, models.Geography)
    if location is None:
        raise HTTPException(status_code=404, detail="No data found")
    return location


@app.get("/company_stock")
def get_company_stock(db: Session = Depends(get_db)):
    company_stock = get_instance(db, models.CompanyStock)
    if company_stock is None:
        raise HTTPException(status_code=404, detail="No data found")
    return company_stock


@app.get("/market_index")
def get_market_index(db: Session = Depends(get_db)):
    market_index = get_instance(db, models.MarketIndex)
    if market_index is None:
        raise HTTPException(status_code=404, detail="No data found")
    return market_index


@app.get("/index_stock")
def get_index_stock(db: Session = Depends(get_db)):
    index_stock = get_instance(db, models.IndexStock)
    if index_stock is None:
        raise HTTPException(status_code=404, detail="No data found")
    return index_stock


@app.get("/gics")
def get_gics_class(db: Session = Depends(get_db)):
    gics_class = get_instance(db, models.GICSClassification)
    if gics_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return gics_class


@app.get("/naics")
def get_naics_class(db: Session = Depends(get_db)):
    naics_class = get_instance(db, models.NAICSClassification)
    if naics_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return naics_class


@app.get("/trbc/")
def get_trbc_class(db: Session = Depends(get_db)):
    trbc_class = get_instance(db, models.TRBCClassification)
    if trbc_class is None:
        raise HTTPException(status_code=404, detail="No data found")
    return trbc_class
