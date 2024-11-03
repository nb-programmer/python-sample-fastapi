import datetime
import uuid

from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String, Uuid

from ...database.base import BaseDBModel


class User(BaseDBModel):
    __tablename__ = "users"

    id: Column[uuid.UUID] = Column(Uuid, primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True)

    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

    created_ts = Column(DateTime, default=datetime.datetime.now)
    updated_ts = Column(DateTime, nullable=True)


# TODO:
# class UserPassword(BaseDBModel):
#     __tablename__ = "user_passwords"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Uuid, ForeignKey(User.id))
#     password_hash = Column(String, nullable=False)
#     created_ts = Column(DateTime, default=datetime.datetime.now)
#     expiry_ts = Column(DateTime, nullable=True)
