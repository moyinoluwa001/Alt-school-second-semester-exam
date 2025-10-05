# This module contains test cases for the enrollment-related API endpoints.
# It verifies the functionality of enrolling users in courses.

from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

def test_enroll_user():
    """Test enrolling a user in a course."""
    user_response = client.post("/users/", json={"name": "Bob", "email": "bob@example.com", "is_active": True})
    user_id = user_response.json()["id"]

    course_response = client.post("/courses/", json={"title": "FastAPI", "description": "API Development", "is_open": True})
    course_id = course_response.json()["id"]

    response = client.post("/enrollments/", json={"user_id": user_id, "course_id": course_id, "enrolled_date": "2025-10-01"})
    assert response.status_code == 200
    assert response.json()["completed"] is False
