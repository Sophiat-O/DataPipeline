import json
import requests
from time import sleep
from .kafka_base_logger import logger
from kafka import KafkaProducer


def produce_company_data():
    try:
        request_comapnies = requests.get("http://localhost:8000/companies")
        companies = request_comapnies.json()
        producer = KafkaProducer(
            bootstrap_servers=["localhost:9093"],
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

        logger.info("Producer Started")

        for company in companies:
            producer.send("company", value=company)
            sleep(1)

    except Exception:
        logger.exception("An exception has occured, try again later")

    return


if __name__ == "__main__":
    produce_company_data()
