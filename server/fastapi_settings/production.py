from typing import List

from .base import Settings as BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    CORS_ORIGINS: List[str] = [
        "https://fletchers-recommended-api-xdpvinwgya-uw.a.run.app",
    ]

    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "fMwo5jy3bx7k7BPr"
    DATABASE_HOST: str = (
        "/cloudsql/calm-bison-321506:us-west1:fletcher-recommended-database"
    )
    DATABASE_NAME: str = "postgres"
