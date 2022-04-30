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

def test_add_stock():
    respone = client.post('stocks/{stock}?new_stock=AAPL')
    assert respone.status_code == 200
    assert respone.json() == {"AAPL": "added succesfully"}

def test_stock_not_found():
    response = client.get("{stock}?symbol=AAPL")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_stock_delete():
    response = client.delete("stocks/{stock}?symbol=AAPL")
    assert response.status_code == 200
    assert response.json() == {'stock AAPL': 'removed successfully'}