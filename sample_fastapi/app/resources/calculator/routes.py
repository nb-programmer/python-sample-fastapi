from fastapi import APIRouter

from .views import calc_dec2hex, calc_hex2dec


def init_routes():
    router = APIRouter(prefix="/calculator", tags=["calculator"])

    router.add_api_route("/convert/dec2hex", calc_dec2hex, methods={"POST"})
    router.add_api_route("/convert/hex2dec", calc_hex2dec, methods={"POST"})

    return router
