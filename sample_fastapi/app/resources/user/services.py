from typing import Annotated
from uuid import UUID

import sqlalchemy
from fastapi import Depends

from ...database import AsyncSession, get_db_session
from . import db_models, db_queries
from .models import UserCreatedResponse, UserCreateError, UserInfoResponse


class UserService:
    """User management service"""

    def __init__(self, db: Annotated[AsyncSession, Depends(get_db_session)]):
        self._db = db

    async def create_user(
        self,
        username: str,
        first_name: str,
        middle_name: str | None = None,
        last_name: str | None = None,
    ) -> UserCreatedResponse:
        """Create a new user (if `username` doesn't exist) with the
        given details and save it in the database.

        :param str username: Username of the new user
        :param str first_name: First name
        :param str or None middle_name: Middle name
        :param str or None last_name: Last name
        :return UserCreatedResponse: Contains the ID of the newly created user

        :raises UserCreateError: If an error occurres while creating the user (Eg. already existing username)"""
        try:
            new_user = db_models.User(
                username=username,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
            )

            self._db.add(new_user)
            await self._db.commit()

            return UserCreatedResponse.model_validate(new_user)
        except sqlalchemy.exc.IntegrityError as ex:
            raise UserCreateError("Username `%s` already exists." % username) from ex

    async def user_query_all(self) -> list[UserInfoResponse]:
        """Returns a list of users that have registered.

        :return list[UserInfoResponse]: A list of `UserInfoResponse` items containing various information about each user
        """
        results = await self._db.scalars(db_queries.QUERY_ALL_USERS)
        user_list = map(UserInfoResponse.model_validate, results.all())
        return list(user_list)

    async def user_query_id(self, user_id: UUID) -> UserInfoResponse | None:
        result = await self._db.scalar(db_queries.QUERY_USER_BY_ID, {"id": user_id})
        if result:
            return UserInfoResponse.model_validate(result)

    async def user_query_username(self, username: str) -> UserInfoResponse | None:
        result = await self._db.scalar(db_queries.QUERY_USER_BY_USERNAME, {"username": username})
        if result:
            return UserInfoResponse.model_validate(result)
