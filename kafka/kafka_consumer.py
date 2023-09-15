import json
import traceback
from data_load.models import *
from confluent_kafka import Consumer, OFFSET_BEGINNING
from kafka_base_logger import logger
from data_load.orm_load import create_instance

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


def consume_data():
    try:
        conf = {
            "bootstrap.servers": "localhost:9093",
            "group.id": "stock_data",
            "enable.auto.commit": True,
            "auto.offset.reset": "smallest",
        }

        consumer = Consumer(conf)

        def assign_reset(consumer, partitions):
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            print("assign", partitions)
            consumer.assign(partitions)

        consumer.subscribe(all_topics, on_assign=assign_reset)

        logger.info("Subcribed to all Topics")

        while True:
            message = consumer.poll()

            topic = message.topic()

            model = json.loads(message.value().decode())

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

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("An exception has occured" + "\n" + error_type)

    return "Staging Database Updated"


if __name__ == "__main__":
    consume_data()
