import os
import traceback
from dotenv import load_dotenv
from data_extract.base_logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


def get_session():
    try:
        db_user = os.getenv("source_db_user")
        password = os.getenv("source_db_pass")
        database = os.getenv("source_db_name")
        host = os.getenv("source_host")

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("Invalid variable in .env file" + "\n" + error_type)

    database_url = (
        "mysql+pymysql://" + db_user + ":" + password + "@" + host + "/" + database
    )

    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal
