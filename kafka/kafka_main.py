import json
import requests
from kafka_producer import produce_data


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

    data = {
        "company": request_comapnies,
        "markets": request_markets,
        "geography": request_geography,
        "company_stock": request_comp_stock,
        "market_index": request_mkt_index,
        "index_stock": request_idx_stock,
        "gics": request_gics,
        "naics": request_naics,
        "trbc": request_trbc,
    }

    for key, values in data.items():
        for value in values:
            produce_data(key, value)

    return "Streamed Data"


if __name__ == "__main__":
    stream_api_endpoint()
