#!/usr/bin/env python3
"""
Defines a BasicAuth class that inherits from Auth class
"""
import uuid
from api.v1.auth.auth import Auth
from api.v1.views.users import User


class SessionAuth(Auth):
    """ Authenticates User Session
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID
        """
        if (
            user_id is None
            or isinstance(user_id, str) is False
        ):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
