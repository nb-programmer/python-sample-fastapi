from contextlib import AsyncExitStack, asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def _dummy_lifespan():
    yield


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncExitStack() as stack:
        await stack.enter_async_context(_dummy_lifespan())
        yield
