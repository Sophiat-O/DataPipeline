import json
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


f = open("/Users/sophie/DataPipeline/DataPipeline/data_app/connection_string.json")
connection_detail = json.load(f)


def get_session():
    try:
        db_user = connection_detail["db_user"]
        password = connection_detail["db_pass"]
        database = connection_detail["db_name"]
        host = connection_detail["host"]
    except NameError:
        logging.error("File Not Found")

    database_url = (
        "mysql+pymysql://" + db_user + ":" + password + "@" + host + "/" + database
    )

    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal
