import logging
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI

from .. import utils
from .config import APP_DB_SESSION_MANAGER_KEY, DBSettings
from .session import AsyncDatabaseSessionManager

LOG = logging.getLogger(__name__)


async def create_schema_models(sessionmanager: AsyncDatabaseSessionManager):
    """Create schema tables from models under `BaseDBModel`."""
    async with sessionmanager._engine.connect() as connection:
        from .base import BaseDBModel

        LOG.info("Creating schema (if not already exists)...")
        LOG.info("DB models registered: [%s]", ",".join(map(utils.str_quote, BaseDBModel.metadata.tables.keys())))

        await connection.run_sync(BaseDBModel.metadata.create_all)
        await connection.commit()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Session manager, manage database connections for this app"""
    sessionmanager: AsyncDatabaseSessionManager = app.extra[APP_DB_SESSION_MANAGER_KEY]
    async with sessionmanager:
        await create_schema_models(sessionmanager)
        yield


def init_app_db(app: FastAPI, db_settings: Annotated[DBSettings, DBSettings()]):
    """Initialize database session manager and bind it with the FastAPI application"""
    app.extra[APP_DB_SESSION_MANAGER_KEY] = AsyncDatabaseSessionManager(
        db_settings.database_url,
        {
            "echo": db_settings.echo_sql,
        },
    )
