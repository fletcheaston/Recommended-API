from typing import List

from .base import Settings as BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ]

    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "super secret password"
    DATABASE_HOST: str = "test-db"
    DATABASE_NAME: str = "postgres"
