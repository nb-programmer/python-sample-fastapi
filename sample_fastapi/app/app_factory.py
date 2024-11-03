import logging
import logging.handlers
from contextlib import AsyncExitStack, asynccontextmanager

from fastapi import FastAPI
from tqdm.contrib.logging import logging_redirect_tqdm

from . import database, middleware, resources

LOG = logging.getLogger(__name__)


@asynccontextmanager
async def app_lifespan_handler(app: FastAPI):
    """Application lifespan handler

    Purpose: Initialize components at startup of the app, and free before shutdown.
    """

    async with AsyncExitStack() as stack:
        LOG.info('Executing lifespan handler for "resources"...')
        await stack.enter_async_context(resources.lifespan(app))
        LOG.info('Executing lifespan handler for "database"...')
        await stack.enter_async_context(database.lifespan(app))
        LOG.info('Executing lifespan handler for "tqdm_logging"...')
        stack.enter_context(logging_redirect_tqdm())
        yield


def init_app():
    db_settings = database.get_db_settings()

    app = FastAPI(lifespan=app_lifespan_handler)

    resources.init_app(app)
    middleware.init_middleware(app)
    database.init_app_db(app, db_settings)

    return app
