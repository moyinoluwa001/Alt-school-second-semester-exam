# This module contains services for managing users.
# It includes functions for creating, retrieving, updating, and deleting users.

from typing import List, Optional
from schemas.user_schema import User
from uuid import uuid4


users_db: List[User] = [
    User(id=str(uuid4()), name="Alice John", email="alice@example.com", is_active=True),
    User(id=str(uuid4()), name="Bob Joe", email="bob@example.com", is_active=True),
    User(id=str(uuid4()), name="Charlie", email="charlie@example.com", is_active=False)
]



def create_user(user_data) -> User:
    """Create a new user and add them to the database."""
    user = User(id=str(uuid4()), **user_data.model_dump())  # Replaced dict() with model_dump()
    users_db.append(user)
    return user

def get_user(user_id: str) -> Optional[User]:
    """Retrieve a user by their ID."""
    return next((u for u in users_db if u.id == user_id), None)

def update_user(user_id: str, updated_user: User) -> Optional[User]:
    """Update the details of an existing user."""
    user = get_user(user_id)
    if user:
        user.name = updated_user.name
        user.email = updated_user.email
        user.is_active = updated_user.is_active  # Added logic to update is_active field
    return user

def deactivate_user(user_id: str) -> Optional[User]:
    """Deactivate a user by their ID."""
    user = get_user(user_id)
    if user:
        user.is_active = False
    return user

def delete_user(user_id: str) -> bool:
    """Delete a user by their ID."""
    global users_db
    users_db = [u for u in users_db if u.id != user_id]
    return True

def get_all_users() -> List[User]:
    """Retrieve all users."""
    return users_db
