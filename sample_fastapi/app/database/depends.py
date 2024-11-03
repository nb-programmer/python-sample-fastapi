from functools import lru_cache
from typing import Annotated

from fastapi import Depends, Request

from .config import APP_DB_SESSION_MANAGER_KEY, DBSettings
from .session import AsyncDatabaseSessionManager


@lru_cache()
def get_db_settings():
    return DBSettings()


def get_app_db_session_manager(req: Request) -> AsyncDatabaseSessionManager:
    sessionmanager: AsyncDatabaseSessionManager | None = req.app.extra.get(APP_DB_SESSION_MANAGER_KEY)
    if sessionmanager is None:
        raise RuntimeError(
            "Couldn't get the app's DB session manager - DB Session Manager with key `%s` was not initialized"
            % APP_DB_SESSION_MANAGER_KEY
        )
    return sessionmanager


async def get_db_session(sessionmanager: Annotated[AsyncDatabaseSessionManager, Depends(get_app_db_session_manager)]):
    """Dependency to get a session object. Use this in request handlers to get a database session."""

    async with sessionmanager.session() as session:
        yield session
