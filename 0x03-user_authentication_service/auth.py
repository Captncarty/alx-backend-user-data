#!/usr/bin/env python3
"""
In this task you will define a _hash_password method that
takes in a password string arguments and returns bytes.
The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
"""

from uuid import uuid4
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    input password hashed with bcrypt.hashpw
    """
    if password:
        salt = gensalt()
        hashed_pwd = hashpw(password.encode('utf-8'), salt)
        return hashed_pwd
    print(f'password: "{password}", fix something in')


def _generate_uuid() -> str:
    """
    Implement a _generate_uuid function in the auth module
    return a string representation of a new UUID
    Use the uuid module.
    method is private to the auth module
    """
    return str(uuid4())


class Auth:
    """
    implement the Auth.register_user in the Auth class provided below:
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        regusters a new user if not existing
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email}  already exists")
        except NoResultFound:
            hashed_pw = _hash_password(password)
            register = self._db.add_user(email, hashed_pw)
            return register

    def valid_login(self, email: str, password: str) -> bool:
        """
        Implement the Auth.valid_login method.
        It should expect email and password required arguments
        and return a boolean.
        locate the user by email.
        If it exists, check the password with bcrypt.checkpw.
        If it matches return True. In any other case, return False.
        """
        try:
            user = self._db.find_user_by(email=email)
            check = checkpw(password.encode('utf-8'), user.hashed_password)
            return check
        except NoResultFound:
            return False


def create_session(self, email: str) -> str:
        """
        Implement the Auth.create_session method
        takes an email string argument and returns the session ID as a string
        The method should find the user corresponding to the email
        generate a new UUID and store it in the database
        as the user’s session_id, then return the session ID.
        Remember that only public methods of self._db can be used.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union(str, None):
        """
        In this task, you will implement the Auth.get_user_from_session_id method.
        It takes a single session_id string argument
        and returns the corresponding User or None.
        If the session ID is None or no user is found,
        return None. Otherwise return the corresponding user.
        Remember to only use public methods of self._db.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None::
        """
        In this task, you will implement Auth.destroy_session.
        The method takes a single user_id integer argument and returns None.
        The method updates the corresponding user’s session ID to None.
        Remember to only use public methods of self._db.
        """
        if user_id is None:
            return None
        try:
            user = self._db.find_user_by(id=user_id)
            return self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Finds user by email, updates user's reset_toke with UUID """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(found_user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Use the reset_token to find the corresponding user.
            If it does not exist, raise a ValueError exception.
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Finds user by email, updates user's reset_toke with UUID """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()
        self._db.update_user(found_user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """ Use the reset_token to find the corresponding user.
            If it does not exist, raise a ValueError exception.
        """
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)