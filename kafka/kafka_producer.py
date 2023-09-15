import json
import traceback
from time import sleep
from kafka_base_logger import logger
from confluent_kafka import Producer
from confluent_kafka import SerializingProducer


def produce_data(topic, value):
    try:
        kafka_config = {
            "bootstrap.servers": "localhost:9093",
            "enable.idempotence": "true",
            "acks": "all",
        }

        producer = Producer(kafka_config)
        logger.info("Producer Started")

        encode_value = json.dumps(value).encode("utf-8")

        producer.produce(topic, encode_value)
        producer.poll(100)
        producer.flush()

    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        error_type = formatted_lines[-1]
        logger.error("An exception has occured" + "\n" + error_type)

    return "Completed"
