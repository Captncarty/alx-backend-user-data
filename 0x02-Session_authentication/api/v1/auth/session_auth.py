#!/usr/bin/env python3
"""
Defines a BasicAuth class that inherits from Auth class
"""
import base64
from typing import Tuple, TypeVar, Union
from api.v1.auth.auth import Auth
from api.v1.views.users import User


class SessionAuth(Auth):
    """ Authenticates User Session
    """
    pass
