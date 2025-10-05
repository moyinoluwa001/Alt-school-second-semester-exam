# This module contains services for managing enrollments, including creating, updating, and retrieving enrollments.

from typing import List, Optional
from schemas.enrollment_schema import Enrollment
from services.user_services import get_user, users_db
from services.course_services import get_course, courses_db
from uuid import uuid4
from datetime import date

# In-memory database for enrollments
enrollments_db: List[Enrollment] = []

def initialize_enrollments():
    """Initialize enrollments with valid user_id and course_id."""
    if users_db and courses_db:
        enrollments_db.extend([
            Enrollment(
                id=str(uuid4()),
                user_id=users_db[0].id,
                course_id=courses_db[0].id,
                enrolled_date=date(2025, 10, 1),
                completed=False
            ),
            Enrollment(
                id=str(uuid4()),
                user_id=users_db[1].id,
                course_id=courses_db[1].id,
                enrolled_date=date(2025, 10, 2),
                completed=True
            )
        ])

def enroll_user(enrollment: Enrollment) -> Optional[str]:
    """Enroll a user in a course with validation checks."""
    user = get_user(enrollment.user_id)
    course = get_course(enrollment.course_id)

    # Validate user and course
    if not user or not user.is_active:
        return "User is not active or does not exist"
    if not course or not course.is_open:
        return "Course is not open or does not exist"

    # Check for duplicate enrollment
    if any(e.user_id == enrollment.user_id and e.course_id == enrollment.course_id for e in enrollments_db):
        return "User already enrolled in this course"

    # Add enrollment to the database
    enrollments_db.append(enrollment)
    return None

def mark_completion(enrollment_id: str) -> Optional[Enrollment]:
    """Mark an enrollment as completed."""
    enrollment = next((e for e in enrollments_db if e.id == enrollment_id), None)
    if enrollment:
        enrollment.completed = True
    return enrollment

def get_user_enrollments(user_id: str) -> List[Enrollment]:
    """Retrieve all enrollments for a specific user."""
    return [e for e in enrollments_db if e.user_id == user_id]

def get_all_enrollments() -> List[Enrollment]:
    """Retrieve all enrollments with valid user_id and course_id."""
    return [
        e for e in enrollments_db
        if get_user(e.user_id) and get_user(e.user_id).is_active
        and get_course(e.course_id) and get_course(e.course_id).is_open
    ]

def get_course_enrollments(course_id: str) -> List[Enrollment]:
    """Retrieve all enrollments for a specific course."""
    return [e for e in enrollments_db if e.course_id == course_id]

# Initialize enrollments with valid data
initialize_enrollments()
