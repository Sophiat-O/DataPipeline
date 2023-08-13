# import sys
from fastapi.testclient import TestClient
from data_app.main import app


client = TestClient(app)


def test_get_companies():
    response = client.get("/companies")
    assert response.status_code == 200


def test_get_markets():
    response = client.get("/markets")
    assert response.status_code == 200


def test_get_geography():
    response = client.get("/geography")
    assert response.status_code == 200
