from typing import Annotated
from uuid import UUID

from fastapi import Depends, Form, HTTPException, status

from .models import UserCreatedResponse, UserCreateError, UserInfoResponse
from .services import UserService


async def user_create(
    user_service: Annotated[UserService, Depends(UserService)],
    username: Annotated[str, Form()],
    first_name: Annotated[str, Form()],
    middle_name: str | None = Form(default=None),
    last_name: str | None = Form(default=None),
) -> UserCreatedResponse:
    try:
        return await user_service.create_user(username, first_name, middle_name, last_name)
    except UserCreateError as ex:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=str(ex)) from ex


async def user_list(user_service: Annotated[UserService, Depends(UserService)]) -> list[UserInfoResponse]:
    return await user_service.user_query_all()


async def user_data(user_service: Annotated[UserService, Depends(UserService)], user_id: UUID):
    user = await user_service.user_query_id(user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User with id `%s` not found." % str(user_id))
    return user
