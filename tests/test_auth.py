import uuid

from django.test import TransactionTestCase
from fastapi.testclient import TestClient
from pydantic import EmailStr

from api.models import DatabaseUser, UserLogin, UserSaved
from api.utils import (
    ensure_anonymous_user,
    get_optional_user,
    get_password_hash,
    get_required_user,
)
from main import app


class AnonymousTests(TransactionTestCase):
    def setUp(self) -> None:
        self.password = f"{uuid.uuid4()}"
        self.user = DatabaseUser.objects.create(
            email="test@gmail.com",
            name="Test User",
            hashed_password=get_password_hash(self.password),
        )

        def ensure_anonymous_user_override() -> None:
            return None

        def get_optional_user_override() -> None:
            return None

        # Dependency override to never return a user for this test client.
        app.dependency_overrides[ensure_anonymous_user] = ensure_anonymous_user_override
        app.dependency_overrides[get_optional_user] = get_optional_user_override
        self.test_client = TestClient(app)

    def test_fails_login_check(self) -> None:
        response = self.test_client.get("/auth")

        assert response.status_code == 401

    def test_successful_login(self) -> None:
        credentials = UserLogin(
            email=self.user.email,
            password=self.password,
        )
        response = self.test_client.post("/auth", data=credentials.json())

        assert response.status_code == 200
        assert UserSaved(**response.json()) == UserSaved.from_orm(self.user)

    def test_fails_login(self) -> None:
        credentials = UserLogin(
            email=EmailStr(f"bad-{self.user.email}"),
            password=self.password,
        )
        response = self.test_client.post("/auth", data=credentials.json())

        assert response.status_code == 400


class AuthenticatedTests(TransactionTestCase):
    def setUp(self) -> None:
        self.password = f"{uuid.uuid4()}"
        self.user = DatabaseUser.objects.create(
            email="test@gmail.com",
            name="Test User",
            hashed_password=get_password_hash(self.password),
        )

        def get_required_user_override() -> DatabaseUser:
            return self.user

        def get_optional_user_override() -> DatabaseUser:
            return self.user

        # Dependency override to always return a user for this test client.
        app.dependency_overrides[get_required_user] = get_required_user_override
        app.dependency_overrides[get_optional_user] = get_optional_user_override
        self.test_client = TestClient(app)

    def test_successful_login_check(self) -> None:
        response = self.test_client.get("/auth")

        assert response.status_code == 200
        assert UserSaved(**response.json()) == UserSaved.from_orm(self.user)

    def test_successful_logout(self) -> None:
        response = self.test_client.delete("/auth")

        assert response.status_code == 200

        # TODO: Ensure this actually removes the cookie so logout really succeeds
