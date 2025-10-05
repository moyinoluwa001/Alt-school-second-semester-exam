# This module defines the Pydantic schemas for users.
# It includes base, creation, and response models for user data.

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Base schema for user data."""
    name: str
    email: EmailStr

class UserCreate(UserBase):
    """Schema for creating a new user."""
    is_active: bool = True  # Added is_active field to allow setting user status during creation

from uuid import uuid4

class User(UserBase):
    """Schema for representing a user with their ID."""
    id: str
    is_active: bool = True
