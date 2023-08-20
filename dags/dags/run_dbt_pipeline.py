import os
import traceback
from airflow import DAG
from dotenv import load_dotenv
from datetime import timedelta
from base_logger import logger
from airflow.utils.dates import days_ago
from airflow.models.baseoperator import chain
from airflow_dbt.operators.dbt_operator import DbtRunOperator, DbtDocsGenerateOperator

load_dotenv()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "start_date": days_ago(1),
    "schedule_interval": "0 0 * * *",
    "dir": os.getenv("dir"),
}


with DAG(
    dag_id="dbt_pipeline",
    default_args=default_args,
) as dag:
    try:
        dbt_run_stock_model = DbtRunOperator(
            task_id="dbt_run_my_stock_model",
            select="stock",
            profiles_dir=default_args["dir"],
            dir=default_args["dir"],
        )

        dbt_run_market_model = DbtRunOperator(
            task_id="dbt_run_my_market_model",
            select="market_stock",
            profiles_dir=default_args["dir"],
            dir=default_args["dir"],
        )

        dbt_docs_generate = DbtDocsGenerateOperator(
            task_id="dbt_docs_generate",
        )

        chain(dbt_run_stock_model, dbt_run_market_model, dbt_docs_generate)

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("An exception occured" + "\n" + error_type)
