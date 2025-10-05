# This module defines the Pydantic schemas for enrollments.
# It includes base, creation, and response models for enrollment data.

from pydantic import BaseModel
from datetime import date

class EnrollmentBase(BaseModel):
    """Base schema for enrollment data."""
    user_id: str
    course_id: str

class EnrollmentCreate(EnrollmentBase):
    """Schema for creating a new enrollment."""
    enrolled_date: date

class Enrollment(EnrollmentBase):
    """Schema for representing an enrollment with its ID and status."""
    id: str
    enrolled_date: date
    completed: bool = False
