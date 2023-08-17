import json
import traceback
from data_load.models import *
from kafka import KafkaConsumer
from kafka import OffsetAndMetadata
from kafka_base_logger import logger
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
            bootstrap_servers=["localhost:9093"],
            group_id="stock_data",
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
        consumer.subscribe(all_topics)

        logger.info("Subcribed to all Topics")

        while True:
            raw_data = consumer.poll(timeout_ms=100)

            for topic_partition, message in raw_data.items():
                topic = topic_partition.topic
                model = message[0].value

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
