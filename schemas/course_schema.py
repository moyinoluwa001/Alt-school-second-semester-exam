# This module defines the Pydantic schemas for courses.
# It includes base, creation, and response models for course data.

from pydantic import BaseModel
from uuid import uuid4

class CourseBase(BaseModel):
    """Base schema for course data."""
    title: str
    description: str

class CourseCreate(CourseBase):
    """Schema for creating a new course."""
    is_open: bool = True

class Course(CourseBase):
    """Schema for representing a course with its ID."""
    id: str
    is_open: bool = True
