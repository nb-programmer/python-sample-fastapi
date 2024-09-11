
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def init_middleware(app: FastAPI):
    # TODO: Allow this to be configurable
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
