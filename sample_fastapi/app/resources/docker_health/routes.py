from fastapi import APIRouter, FastAPI

from .views import respond_healthcheck


def init_routes():
    router = APIRouter(prefix="/health", tags=["health"])

    router.add_api_route("/healthcheck", respond_healthcheck, methods={"GET"})

    return router


def init_app(app: FastAPI):
    app.include_router(init_routes())
