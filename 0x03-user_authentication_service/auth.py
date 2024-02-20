#!/usr/bin/env python3
"""
Auth module
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
