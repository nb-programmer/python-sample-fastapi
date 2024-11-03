import logging
from functools import lru_cache

from pydantic import Field

from ..config import BaseAppSettings

LOG = logging.getLogger(__name__)

APP_DB_SESSION_MANAGER_KEY = "_dbsm"  # Lol


@lru_cache()
def _default_db_dsn():
    LOG.warning(
        "Using SQLite In-memory database as `database_url` config was not specified. Content WILL be lost after shutting down the app!"
    )
    return "sqlite+aiosqlite:///:memory:"


class DBSettings(BaseAppSettings):
    database_url: str = Field(default_factory=_default_db_dsn)
    echo_sql: bool = Field(default=True)
