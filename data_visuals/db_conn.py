import os
import traceback
from dotenv import load_dotenv
from data_visuals.base_logger import logger
from sqlalchemy import create_engine

load_dotenv()


def get_engine():
    try:
        db_user = os.getenv("viz_db_user")
        password = os.getenv("viz_db_pass")
        database = os.getenv("viz_db_name")
        host = os.getenv("viz_host")

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

    return engine
