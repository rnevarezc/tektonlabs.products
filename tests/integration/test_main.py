import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "title": "This is the products microservice",
        "version": "1.0.0"
    }
