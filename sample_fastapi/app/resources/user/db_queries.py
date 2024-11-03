from sqlalchemy import bindparam, insert, select

from .db_models import User

QUERY_ALL_USERS = select(User)

QUERY_USER_BY_ID = QUERY_ALL_USERS.where(User.id == bindparam("id"))
QUERY_USER_BY_USERNAME = QUERY_ALL_USERS.where(User.username == bindparam("username"))
