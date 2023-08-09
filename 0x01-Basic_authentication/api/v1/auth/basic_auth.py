#!/usr/bin/env python3
"""
Defines a BasicAuth class that inherits from Auth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication that inherits from authentication
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """ Extract the authorization header
        """
        if (
            authorization_header is None
            or type(authorization_header) != str
            or not authorization_header.startswith('Basic ')
        ):
            return None
        return ''.join(authorization_header.split('Basic ')[1:])
