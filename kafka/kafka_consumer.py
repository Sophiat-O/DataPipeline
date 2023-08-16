import json
import traceback
from kafka import KafkaConsumer
from data_load.models import *
from .kafka_base_logger import logger
from data_load.orm_load import create_instance


def consume_data():
    all_topics = [
        "company",
        "markets",
        "geography",
        "company_stock",
        "market_index",
        "index_stock",
        "gics",
        "naics",
        "trbc",
    ]

    try:
        consumer = KafkaConsumer(
            all_topics,
            bootstrap_servers=["localhost:9093"],
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )

        logger.info("Now Consuming")

        for message in consumer:
            topic = message.topic
            model = message.value

            if topic == "company":
                create_instance(STGCompany, model)
            elif topic == "markets":
                create_instance(STGMarket, model)
            elif topic == "geography":
                create_instance(STGGeography, model)
            elif topic == "company_stock":
                create_instance(STGCompanyStock, model)
            elif topic == "market_index":
                create_instance(STGMarketIndex, model)
            elif topic == "index_stock":
                create_instance(STGIndexStock, model)
            elif topic == "gics":
                create_instance(STGGICSClassification, model)
            elif topic == "naics":
                create_instance(STGNAICSClassification, model)
            else:
                create_instance(STGTRBCClassification, model)

        consumer.close()

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("An exception has occured" + "\n" + error_type)

    return "Staging Database Updated"


if __name__ == "__main__":
    consume_data()
