from functools import lru_cache

from fastapi.testclient import TestClient


@lru_cache()
def get_app():
    from sample_fastapi.app.app_factory import init_app

    return init_app()


def get_test_client():
    return TestClient(get_app())
