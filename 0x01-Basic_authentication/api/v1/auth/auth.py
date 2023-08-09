#!/usr/bin/env python3
""" Creating a class to manage the API authentication
"""
from typing import (
    List,
    TypeVar
)
from flask import request
from models.user import User


class Auth:
    """ API authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path
        """
        if path is None or not excluded_paths:
            return True
        for i in excluded_paths:
            if i.endswith('*') and path.startswith(i[:-1]):
                return False
            elif i in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ returns None - path
        """
        auth = request.headers.get('Authorization', None) if request else None
        if request is None or auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None - request
        """
        return None