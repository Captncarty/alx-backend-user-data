#!/usr/bin/env python3
"""
In this task you will define a _hash_password method that
takes in a password string arguments and returns bytes.
The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
"""

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
