# tests/test_expected_failure.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_expected_failure_example():
    # Teste que inicialmente vai falhar se você ainda não tiver a lógica pedida:
    # por exemplo espera que GET /items/1 tenha "name" igual a "Item 1"
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json().get("name") == "Item 1"
