# This module contains test cases for the user-related API endpoints.
# It verifies the functionality of creating and managing users.

from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

def test_create_user():
    """Test the creation of a new user."""
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com", "is_active": True})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["is_active"] is True
