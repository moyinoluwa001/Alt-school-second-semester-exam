# This module contains test cases for the course-related API endpoints.
# It verifies the functionality of creating and managing courses.

from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

def test_create_course():
    """Test the creation of a new course."""
    response = client.post("/courses/", json={"title": "Python Basics", "description": "Learn Python", "is_open": True})
    assert response.status_code == 200
    assert response.json()["title"] == "Python Basics"
    assert response.json()["is_open"] is True
