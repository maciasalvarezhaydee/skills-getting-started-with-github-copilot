import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Puedes ajustar el contenido esperado según tu endpoint
    assert "Hello" in response.text
