from typing import Any

from django.conf import settings
from django.db import connection
from django.test.runner import DiscoverRunner


class TestRunner(DiscoverRunner):
    def teardown_databases(self, old_config: Any, **kwargs: Any) -> None:
        # This is necessary because either FastAPI/Starlette or Django's ORM
        # isn't cleaning up the connections after it's done with them.
        # The query below kills all database connections before
        # dropping the database.
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT
                pg_terminate_backend(pid) FROM pg_stat_activity WHERE
                pid <> pg_backend_pid() AND
                pg_stat_activity.datname =
                  '{settings.DATABASES["default"]["NAME"]}';"""
            )
        super().teardown_databases(old_config, **kwargs)
