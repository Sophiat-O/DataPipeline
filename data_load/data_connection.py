import os
import traceback
from dotenv import load_dotenv
from .base_logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


def get_session():
    try:
        db_user = os.getenv("target_db_user")
        password = os.getenv("target_db_pass")
        database = os.getenv("target_db_name")
        host = os.getenv("target_host")

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("Invalid variables in .env file" + "\n" + error_type)

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
