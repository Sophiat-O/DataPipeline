import json
from kafka import KafkaConsumer
from data_load.models import *
from .kafka_base_logger import logger
from data_load.orm_load import create_instance


def consume_company_data():
    try:
        consumer = KafkaConsumer(
            "company",
            bootstrap_servers=["localhost:9093"],
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )

        logger.info("Now Consuming")

        for message in consumer:
            company_dict = message.value
            stg_company = create_instance(STGCompany, company_dict)

    except Exception:
        logger.exception("An exception as occured, try again later")

    return stg_company


if __name__ == "__main__":
    consume_company_data()
