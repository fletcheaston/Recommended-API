import os
from functools import lru_cache
from typing import Dict, Optional, Type

from .fastapi_settings.base import Settings as BaseSettings
from .fastapi_settings.local import Settings as LocalSettings
from .fastapi_settings.production import Settings as ProductionSettings
from .fastapi_settings.test import Settings as TestSettings


@lru_cache(maxsize=None)
def get_settings() -> BaseSettings:
    available_settings: Dict[Optional[str], Type[BaseSettings]] = {
        None: LocalSettings,
        "local": LocalSettings,
        "test": TestSettings,
        "production": ProductionSettings,
    }

    environment = os.getenv("ENV_SETTINGS")

    return available_settings[environment]()


SETTINGS: BaseSettings = get_settings()
