#!/usr/bin/env python3
"""Encryption password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    A function to hash the input password and return the hashed bytes.
    Parameters:
        password (str): The input password to be hashed.
    Returns:
        bytes: The hashed password in bytes.
    """
    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if the provided password matches the hashed password by using bcrypt.

    :param hashed_password: A bytes object representing the hashed password
    :param password: A string representing the plain text password
    :return: A boolean indicating whether the password matches
    the hashed password
    """
    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
