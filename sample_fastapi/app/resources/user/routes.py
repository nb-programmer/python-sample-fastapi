from fastapi import APIRouter, FastAPI

from .views import user_create, user_data, user_list


def init_routes():
    router = APIRouter(prefix="/user", tags=["user"])

    router.add_api_route("/register", user_create, methods={"POST"})
    router.add_api_route("/list", user_list, methods={"GET"})
    router.add_api_route("/{user_id}", user_data, methods={"GET"})

    return router


def init_app(app: FastAPI):
    app.include_router(init_routes())

    # Bind models
    from . import db_models  # noqa
