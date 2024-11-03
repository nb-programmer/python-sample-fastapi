from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UserCreatedResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: UUID = Field(validation_alias="id")
    username: str


class UserInfoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: UUID = Field(validation_alias="id")
    username: str
    first_name: str
    middle_name: str | None
    last_name: str | None


class UserCreateError(ValueError):
    pass
