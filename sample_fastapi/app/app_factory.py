import logging
import logging.handlers
from contextlib import AsyncExitStack, asynccontextmanager

from fastapi import FastAPI
from tqdm.contrib.logging import logging_redirect_tqdm

from . import resources

LOG = logging.getLogger(__name__)


@asynccontextmanager
async def app_lifespan_handler(app: FastAPI):
    """Application lifespan handler

    Purpose: Initialize components at startup of the app, and free before shutdown.
    """

    async with AsyncExitStack() as stack:
        LOG.info('Adding lifespan handler for "resources"...')
        await stack.enter_async_context(resources.lifespan(app))
        LOG.info('Adding lifespan handler for "tqdm_logging"...')
        stack.enter_context(logging_redirect_tqdm())
        yield


def init_app():
    app = FastAPI(lifespan=app_lifespan_handler)
    resources.init_routes(app)
    return app
