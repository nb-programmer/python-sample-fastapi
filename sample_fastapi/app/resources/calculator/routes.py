from fastapi import APIRouter

from .views import conv_dec2hex, conv_hex2dec


def init_routes():
    router = APIRouter(prefix="/calculator", tags=["calculator"])

    router.add_api_route("/convert/dec2hex", conv_dec2hex, methods={"POST"})
    router.add_api_route("/convert/hex2dec", conv_hex2dec, methods={"POST"})

    return router
