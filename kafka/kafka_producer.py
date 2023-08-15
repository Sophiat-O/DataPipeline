import requests
import json
from time import sleep
from json import dumps
from kafka import KafkaProducer


def produce_company_data():
    request_comapnies = requests.get("localhost:8000/companies")

    companies = request_comapnies.json()

    producer = KafkaProducer(
        bootstrap_servers=["kafka:9093"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    for company in companies:
        producer.send("company", value=company)
        sleep(1)

    return
