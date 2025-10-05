# This module defines the API endpoints for managing enrollments.
# It includes functionality for enrolling users in courses and retrieving enrollment details.

from fastapi import APIRouter, HTTPException
from typing import List
from schemas.enrollment_schema import Enrollment, EnrollmentCreate
from uuid import uuid4
from services.enrollment_services import (
    enroll_user, mark_completion, get_user_enrollments, get_all_enrollments
)
from services.user_services import get_user
from services.course_services import get_course

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=Enrollment)
def enroll(enrollment: EnrollmentCreate):
    """Enroll a user in a course with validation."""
    user = get_user(enrollment.user_id)
    course = get_course(enrollment.course_id)

    if not user or not user.is_active:
        raise HTTPException(status_code=400, detail="User is not active or does not exist")
    if not course or not course.is_open:
        raise HTTPException(status_code=400, detail="Course is not open or does not exist")

    existing_enrollments = get_user_enrollments(enrollment.user_id)
    if any(e.course_id == enrollment.course_id for e in existing_enrollments):
        raise HTTPException(status_code=400, detail="User is already enrolled in this course")

    new_enrollment = Enrollment(id=str(uuid4()), **enrollment.model_dump())
    error = enroll_user(new_enrollment)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return new_enrollment

@router.patch("/{enrollment_id}/complete", response_model=Enrollment)
def complete(enrollment_id: str):
    enrollment = mark_completion(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.get("/user/{user_id}", response_model=List[Enrollment])
def user_enrollments(user_id: str):
    return get_user_enrollments(user_id)

@router.get("/", response_model=List[Enrollment])
def all_enrollments():
    return get_all_enrollments()
