# This module defines the API endpoints for managing courses.
# It includes CRUD operations and additional functionality like viewing enrolled users.

from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.logger import logger

from schemas.course_schema import Course, CourseCreate
from schemas.user_schema import User
from services.course_services import (
    create_course,
    get_course,
    update_course,
    close_enrollment,
    delete_course,
)
from services.enrollment_services import get_course_enrollments
from services.user_services import get_user

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.post("/", response_model=Course)
def add_course(course: CourseCreate):
    """Create a new course."""
    created_course = create_course(course)
    return created_course


@router.get("/{course_id}", response_model=Course)
def read_course(course_id: str):
    """Retrieve a course by its ID."""
    course = get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.put("/{course_id}", response_model=Course)
def modify_course(course_id: str, course: CourseCreate):
    """Update a course's details."""
    updated = update_course(course_id, Course(id=course_id, **course.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated


@router.patch("/{course_id}/close", response_model=Course)
def close(course_id: str):
    course = close_enrollment(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.delete("/{course_id}")
def remove_course(course_id: str):
    """Delete a course by its ID."""
    delete_course(course_id)
    return {"message": "Course deleted"}


@router.get("/{course_id}/users", response_model=List[User])
def get_users_in_course(course_id: str):
    """Retrieve all users enrolled in a particular course."""
    enrollments = get_course_enrollments(course_id)
    users = [get_user(enrollment.user_id) for enrollment in enrollments if get_user(enrollment.user_id)]
    return users
