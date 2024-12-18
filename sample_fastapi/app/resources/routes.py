from fastapi import FastAPI


def init_app(app: FastAPI):
    """Initialize routes, middleware, sub-apps, etc. to the given Application"""
    from . import calculator, hello, user
    hello.init_app(app)
    calculator.init_app(app)
    user.init_app(app)
