import json
import traceback
from time import sleep
from .kafka_base_logger import logger
from kafka import KafkaProducer


def produce_data(topic, topic_value):
    try:
        producer = KafkaProducer(
            bootstrap_servers=["localhost:9093"],
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        logger.info("Producer Started")

        producer.send(topic, topic_value)
        sleep(1)
        producer.flush()

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("An exception has occured" + "\n" + error_type)

    return "Completed"
