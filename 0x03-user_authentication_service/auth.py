#!/usr/bin/env python3
"""
Auth module
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    A function to hash the input password and return the hashed bytes.
    Parameters:
           password (str): The input password to be hashed.
    Returns:
           bytes: The hashed password in bytes.
    """
    if password:
        return hashpw(str.encode(password), gensalt())
    return None


def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(str.encode(password), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
