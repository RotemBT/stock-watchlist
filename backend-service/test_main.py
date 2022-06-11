from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello":"world"}

def test_stocklist():
    response = client.get("/stocks")
    assert response.status_code == 200
