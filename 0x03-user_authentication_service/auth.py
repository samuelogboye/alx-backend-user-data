#!/usr/bin/env python3
"""
Auth module
"""
from bcrypt import hashpw, gensalt


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
