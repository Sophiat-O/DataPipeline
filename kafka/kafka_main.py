import json
import requests
from .kafka_producer import produce_data


def stream_api_endpoint():
    request_comapnies = requests.get("http://localhost:8000/companies").json()
    request_markets = requests.get("http://localhost:8000/markets").json()
    request_geography = requests.get("http://localhost:8000/geography").json()
    request_comp_stock = requests.get("http://localhost:8000/company_stock").json()
    request_mkt_index = requests.get("http://localhost:8000/market_index").json()
    request_idx_stock = requests.get("http://localhost:8000/index_stock").json()
    request_gics = requests.get("http://localhost:8000/gics").json()
    request_naics = requests.get("http://localhost:8000/naics").json()
    request_trbc = requests.get("http://localhost:8000/trbc").json()

    for company in request_comapnies:
        produce_data("company", company)

    for market in request_markets:
        produce_data("markets", market)

    for geo in request_geography:
        produce_data("geography", geo)

    for comp_stock in request_comp_stock:
        produce_data("company_stock", comp_stock)

    for mkt_index in request_mkt_index:
        produce_data("market_index", mkt_index)

    for idx_stock in request_idx_stock:
        produce_data("index_stock", idx_stock)

    for gics in request_gics:
        produce_data("gics", gics)

    for naics in request_naics:
        produce_data("naics", naics)

    for trbc in request_trbc:
        produce_data("trbc", trbc)

    return "Streamed Data"


if __name__ == "__main__":
    stream_api_endpoint()
