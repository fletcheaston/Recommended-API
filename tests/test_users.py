import uuid

from django.test import TransactionTestCase
from fastapi.testclient import TestClient
from pydantic import EmailStr

from api.models import DatabaseUser, UserCreate, UserSaved
from api.utils import get_password_hash, get_required_user
from main import app


class UserCreateTests(TransactionTestCase):
    def setUp(self) -> None:
        self.test_client = TestClient(app)

    def test_successful_create_user(self) -> None:
        schema = UserCreate(
            email=EmailStr(f"{uuid.uuid4()}@gmail.com"),
            name="Test User",
            password=f"{uuid.uuid4()}",
        )

        response = self.test_client.post("/users", data=schema.json())

        assert response.status_code == 200

        response_user = UserSaved(**response.json())

        assert schema.email == response_user.email
        assert schema.name == response_user.name

    def test_fails_create_user_duplicate_email(self) -> None:
        schema = UserCreate(
            email=EmailStr(f"{uuid.uuid4()}@gmail.com"),
            name="Test User",
            password=f"{uuid.uuid4()}",
        )

        # Create the user so the endpoint fails.
        DatabaseUser.objects.create(
            email=schema.email,
            name=schema.name,
            hashed_password=get_password_hash(schema.password),
        )

        response = self.test_client.post("/users", data=schema.json())

        assert response.status_code == 400


class UserDeleteTests(TransactionTestCase):
    def setUp(self) -> None:
        self.password = f"{uuid.uuid4()}"
        self.user = DatabaseUser.objects.create(
            email="test@gmail.com",
            name="Test User",
            hashed_password=get_password_hash(self.password),
        )

        def get_required_user_override() -> DatabaseUser:
            return self.user

        # Dependency override to always return a user for this test client.
        app.dependency_overrides[get_required_user] = get_required_user_override
        self.test_client = TestClient(app)

    def test_successful_delete_user(self) -> None:
        assert DatabaseUser.objects.all().count() == 1

        response = self.test_client.delete("/users")

        assert response.status_code == 200
        assert DatabaseUser.objects.all().count() == 0
