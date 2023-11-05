from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

"""
Testing ...
"""
def test_hallo_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}