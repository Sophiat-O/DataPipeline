import json
from .base_logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


def get_session():
    try:
        f = open(
            "/Users/sophie/DataPipeline/DataPipeline/data_load/connection_string.json"
        )
        connection_detail = json.load(f)
        db_user = connection_detail["db_user"]
        password = connection_detail["db_pass"]
        database = connection_detail["db_name"]
        host = connection_detail["host"]
    except Exception:
        logger.exception("File Not Found")

    database_url = (
        "postgresql+psycopg2://"
        + db_user
        + ":"
        + password
        + "@"
        + host
        + "/"
        + database
    )

    engine = create_engine(database_url)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return Session
