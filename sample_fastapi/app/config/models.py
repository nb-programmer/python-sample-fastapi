from functools import partial
from pathlib import Path

import platformdirs
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict

from .settings import APP_NAME


class BaseAppSettings(BaseSettings):
    """Base class for all settings classes. Allows to be loaded from a `.env` file if found."""
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.dev"),
        env_file_encoding="utf-8",
        extra="allow",
    )


class AppSettings(BaseAppSettings):
    """Main application-specific settings"""
    app_base_url: AnyUrl = "http://localhost:8000"


class AppDirectories(BaseAppSettings):
    """Paths that may be used by the application"""
    cache_dir: Path = Field(default_factory=partial(platformdirs.user_cache_path, appname=APP_NAME))
    data_dir: Path = Field(default_factory=partial(platformdirs.user_data_path, appname=APP_NAME))
