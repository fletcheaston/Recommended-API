from pathlib import Path
from typing import Any, Dict, List

from .config import SETTINGS

# We're a little deep into the filesystem, gotta point to where manage.py is.
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key isn't actually used anywhere, FastAPI is handling all of the server security.
SECRET_KEY: str = "django-insecure"
DEBUG: bool = SETTINGS.DEBUG
BACKEND_CORS_ORIGINS: List[str] = SETTINGS.CORS_ORIGINS

# Postgres for our database, and our lone application.
INSTALLED_APPS: List[str] = [
    "django.contrib.postgres",
    "api.apps.BackendConfig",
]

DATABASES: Dict[str, Any] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": SETTINGS.DATABASE_NAME,
        "USER": SETTINGS.DATABASE_USER,
        "PASSWORD": SETTINGS.DATABASE_PASSWORD,
        "HOST": SETTINGS.DATABASE_HOST,
        "PORT": SETTINGS.DATABASE_PORT,
    }
}

TEST_RUNNER = "tests.runner.TestRunner"

# Used to make Django happy.
DEFAULT_TABLESPACE: str = ""
ABSOLUTE_URL_OVERRIDES: Dict[str, Any] = {}
DATABASE_ROUTERS: List[str] = []

# Internationalization, also required to make Django happy.
LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True
