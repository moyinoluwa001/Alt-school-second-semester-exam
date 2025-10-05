# This module contains services for managing courses.
# It includes functions for creating, retrieving, updating, and deleting courses.

from typing import List, Optional
from schemas.course_schema import Course
from uuid import uuid4

courses_db: List[Course] = [
    Course(id=str(uuid4()), title="Math 101", description="Basic Mathematics", is_open=True),
    Course(id=str(uuid4()), title="History 201", description="World History", is_open=True),
    Course(id=str(uuid4()), title="Physics 301", description="Advanced Physics", is_open=False)
]



def create_course(course_data) -> Course:
    """Create a new course and add it to the database."""
    course = Course(id=str(uuid4()), **course_data.model_dump())  # Replaced dict() with model_dump()
    courses_db.append(course)
    return course

def get_course(course_id: str) -> Optional[Course]:
    """Retrieve a course by its ID."""
    return next((c for c in courses_db if c.id == course_id), None)

def update_course(course_id: str, updated_course: Course) -> Optional[Course]:
    """Update the details of an existing course."""
    course = get_course(course_id)
    if course:
        course.title = updated_course.title
        course.description = updated_course.description
        course.is_open = updated_course.is_open  # Allow updating the is_open field
    return course

def close_enrollment(course_id: str) -> Optional[Course]:
    """Close enrollment for a course."""
    course = get_course(course_id)
    if course:
        course.is_open = False
    return course

def delete_course(course_id: str) -> bool:
    """Delete a course by its ID."""
    global courses_db
    courses_db = [c for c in courses_db if c.id != course_id]
    return True

def get_all_courses() -> List[Course]:
    """Retrieve all courses."""
    return courses_db
