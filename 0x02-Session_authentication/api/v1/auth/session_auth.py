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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a User ID based on Session ID
        """
        if (
            session_id is None
            or isinstance(session_id, str) is False
        ):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes the user session/logout
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)

        if cookie is None or self.user_id_for_session_id(cookie) is None:
            return False

        del self.user_id_by_session_id[cookie]
        return True
