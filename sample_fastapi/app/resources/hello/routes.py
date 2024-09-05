from fastapi import APIRouter, FastAPI

from .views import respond_hello, respond_name_greet


def init_routes():
    router = APIRouter(prefix="/hello", tags=["hello"])

    router.add_api_route("", respond_hello, methods={"GET"})
    router.add_api_route("/greet", respond_name_greet, methods={"GET"})

    return router


def init_app(app: FastAPI):
    app.include_router(init_routes())
