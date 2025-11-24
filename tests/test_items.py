# tests/test_items.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_existing_item():
    # Caso de sucesso: GET /items/1 deve retornar status 200 e um JSON com id e name
    response = client.get("/items/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data


def test_get_nonexistent_item():
    # Caso de falha esperada: GET /items/999 deve retornar 404 e detail específico
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não existe"}
