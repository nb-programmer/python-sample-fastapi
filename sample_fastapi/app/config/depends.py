from functools import lru_cache

from .models import AppDirectories, AppSettings


@lru_cache()
def get_app_settings():
    return AppSettings()


@lru_cache()
def get_app_dirs():
    return AppDirectories()
