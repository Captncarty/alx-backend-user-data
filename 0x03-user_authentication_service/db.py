#!/usr/bin/env python3
""" DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add user to db
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        returns the first row found in the users table
        as filtered by the method’s input arguments
        """
        try:
            details = self._session.query(User).filter_by(**kwargs).first()
        except TypeError as exc:
            raise InvalidRequestError from exc
        if details is None:
            raise NoResultFound
        return details

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        implement the DB.update_user method that takes as argument a required
        user_id integer and arbitrary keyword arguments, and returns None.

        The method will use find_user_by to locate the user to update,
        then will update the user’s attributes as passed in the method’s
        arguments then commit changes to the database.
        if argument doesn't correspond, raise ValueError"""
        user_detail = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(user_detail, key):
                setattr(user_detail, key, value)
            else:
                raise ValueError

        self._session.commit()
        return None
