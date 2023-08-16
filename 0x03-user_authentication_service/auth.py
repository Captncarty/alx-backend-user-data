#!/usr/bin/env python3
"""
In this task you will define a _hash_password method that
takes in a password string arguments and returns bytes.
The returned bytes is a salted hash of the input password,
hashed with bcrypt.hashpw.
"""

from bcrypt import gensalt, hashpw


def _hash_password(password):
    """
    input password hashed with bcrypt.hashpw
    """
    if password:
        salt = gensalt()
        hashed_pwd = hashpw(password.encode('utf-8'), salt)
        return hashed_pwd
    print(f'password: "{password}", fix something in')
