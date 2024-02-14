#!/usr/bin/env python3

from api.v1.auth.auth import Auth
from models.user import User

class SessionAuth(Auth):
    """Session Authentication"""
    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = super().create_session(user_id)
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns the User ID by requesting the User ID based on session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        user_id = super().user_id_for_session_id(session_id)
        return user_id

    def current_user(self, request=None) -> User:
        """Returns a User instance based on a cookie value"""
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id:
            return User.get(user_id)
        return None
