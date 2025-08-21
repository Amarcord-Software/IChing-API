import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API del I Ching"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_hexagram():
    response = client.get("/api/v1/hexagrams/1")
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 1
    assert data["name"] == "Ch'ien / Lo Creativo"

def test_get_nonexistent_hexagram():
    response = client.get("/api/v1/hexagrams/99")
    assert response.status_code == 404

def test_consult_oracle():
    response = client.post("/api/v1/consult", json={"question": "¿Cuál es mi camino?"})
    assert response.status_code == 200
    data = response.json()
    assert "lines" in data
    assert "primary_hexagram" in data
    assert len(data["lines"]) == 6