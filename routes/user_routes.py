# This module defines the API endpoints for managing users.
# It includes CRUD operations and additional functionality like deactivating users.

from fastapi import APIRouter, HTTPException
from schemas.user_schema import User, UserCreate
from services.user_services import create_user, get_user, update_user, deactivate_user, delete_user, users_db
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
def add_user(user: UserCreate):
    """Create a new user."""
    created_user = create_user(user)
    return created_user

@router.get("/{user_id}", response_model=User)
def read_user(user_id: str):
    """Retrieve a user by their ID."""
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def modify_user(user_id: str, user: UserCreate):
    """Update a user's details."""
    updated = update_user(user_id, User(id=user_id, **user.dict()))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.patch("/{user_id}/deactivate", response_model=User)
def deactivate(user_id: str):
    """Deactivate a user by their ID."""
    user = deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def remove_user(user_id: str):
    """Delete a user by their ID."""
    delete_user(user_id)
    return {"message": "User deleted"}
