#!/usr/bin/env python3
""" Creating a class to manage the API authentication
"""

from flask import Flask, request
from models.user import User


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns False - path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ returns None - path
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None - request
        """
        return None

