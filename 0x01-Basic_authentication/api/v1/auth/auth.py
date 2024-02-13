#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth"""
        if path is None or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ Authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user"""
        return None
