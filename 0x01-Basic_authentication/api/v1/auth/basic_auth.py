#!/usr/bin/env python3
"""
Defines a BasicAuth class that inherits from Auth class
"""
import base64
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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ returns the decoded value of a Base64 string
        """
        if (
            base64_authorization_header is None
            or type(base64_authorization_header) != str
        ):
            return None

        try:
            encode = base64.b64decode(base64_authorization_header)
            return encode.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ that returns the user email and password
            from the Base64 decoded value.
        """
        if (
            decoded_base64_authorization_header is None
            or type(decoded_base64_authorization_header) != str
            or ':' not in decoded_base64_authorization_header
        ):
            return None, None
        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], ':'.join(credentials[1:])
