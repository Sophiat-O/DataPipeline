from sqlalchemy import Column, ForeignKey, String, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"

    id_company = Column(String, primary_key=True, index=True)
    business_summary = Column(String)
    company_name = Column(String)
    primary_instrument = Column(String)
    ipo_date = Column(Date)
    organization_id = Column(BigInteger)
    organization_website = Column(String)
    trbc_activity_code = Column(
        BigInteger, ForeignKey("trbc_classification.trbc_activity_code")
    )
    gics_subindustry_code = Column(
        BigInteger, ForeignKey("gics_classification.gics_subindustry_code")
    )
    naics_national_industry_code = Column(
        BigInteger, ForeignKey("naics_classification.naics_national_industry_code")
    )
    registration_address_citycode = Column(String, ForeignKey("geography.city_code"))
    hq_address_citycode = Column(String, ForeignKey("geography.city_code"))
    legal_address_citycode = Column(String)
    org_founded_date = Column(Date)


class Geography(Base):
    __tablename__ = "geography"

    city_code = Column(String, primary_key=True, index=True)
    city = Column(String)
    state_province = Column(String)
    country_code_iso = Column(String)
    country = Column(String)
    minor_region = Column(String)
    region = Column(String)


class Market(Base):
    __tablename__ = "market"

    id_market = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    city_code = Column(String, ForeignKey("geography.city_code"))
    founded_date = Column(Date)
    currency = Column(String)
    website = Column(String)


class CompanyStock(Base):
    __tablename__ = "company_stock"

    id_company = Column(String, ForeignKey("company.id_company"), primary_key=True)
    id_market = Column(String, ForeignKey("market.id_market"), primary_key=True)
    price_close_date = Column(Date)
    price_close = Column(BigInteger)
    price_open = Column(BigInteger)
    volume = Column(BigInteger)
    price_high = Column(BigInteger)
    price_low = Column(BigInteger)


class MarketIndex(Base):
    __tablename__ = "market_index"

    id_index = Column(String, primary_key=True, index=True)
    index_name = Column(String)
    index_full_name = Column(String)
    index_description = Column(String)
    create_date = Column(Date)
    id_market = Column(String, ForeignKey("market.id_market"))


class IndexStock(Base):
    __tablename__ = "index_stock"

    id_index = Column(String, ForeignKey("market_index.id_market"), primary_key=True)
    price_close_date = Column(Date)
    price_close = Column(BigInteger)
    price_open = Column(BigInteger)
    volume = Column(BigInteger)
    price_high = Column(BigInteger)
    price_low = Column(BigInteger)


class GICSClassification(Base):
    __tablename__ = "gics_classification"

    gics_subindustry_code = Column(BigInteger, primary_key=True, index=True)
    gics_subindustry = Column(String)
    gics_industry_code = Column(BigInteger)
    gics_industry = Column(String)
    gics_industry_group_code = Column(BigInteger)
    gics_industry_group = Column(String)
    gics_sector_code = Column(BigInteger)
    gics_sector = Column(String)


class NAICSClassification(Base):
    __tablename__ = "naics_classification"

    naics_national_industry_code = Column(BigInteger, primary_key=True, index=True)
    naics_national_industry = Column(String)
    naics_international_industry_code = Column(BigInteger)
    naics_international_industry = Column(String)
    naics_industry_group_code = Column(BigInteger)
    naics_industry_group = Column(String)
    naics_subsector_code = Column(BigInteger)
    naics_subsector = Column(String)
    naics_sector_code = Column(BigInteger)
    naics_sector = Column(String)


class TRBCClassification(Base):
    __tablename__ = "trbc_classification"

    trbc_activity_code = Column(BigInteger, primary_key=True, index=True)
    trbc_activity = Column(String)
    trbc_industry_code = Column(BigInteger)
    trbc_industry = Column(String)
    trbc_industry_group_code = Column(BigInteger)
    trbc_industry_group = Column(String)
    trbc_business_sector_code = Column(BigInteger)
    trbc_business_sector = Column(String)
    trbc_econ_sector_code = Column(BigInteger)
    trbc_econ_sector = Column(String)
