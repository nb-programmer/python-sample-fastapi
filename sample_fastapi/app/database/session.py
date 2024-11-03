import contextlib
import logging
from typing import Any, AsyncIterator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

__all__ = [
    "AsyncConnection",
    "AsyncSession",
    "AsyncDatabaseSessionManager",
]


LOG = logging.getLogger(__name__)


# Heavily inspired by https://praciano.com.br/fastapi-and-async-sqlalchemy-20-with-pytest-done-right.html


class AsyncDatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}, session_kwargs: dict[str, Any] = {}):
        session_kwargs.setdefault("autocommit", False)
        session_kwargs.setdefault("expire_on_commit", False)

        self._engine: AsyncEngine = create_async_engine(host, **engine_kwargs)
        self._sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=self._engine, **session_kwargs)

    async def close(self):
        await self._engine.dispose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                LOG.exception("DB connection was rolled back due to an exception:")
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        async with self._sessionmaker() as sess:
            yield sess
            # try:
            # except Exception:
            #     LOG.exception("DB transaction was rolled back due to an exception:")
            #     # TODO: Not sure if this is needed. Test if it does auto-rollback
            #     await sess.rollback()
            #     raise
