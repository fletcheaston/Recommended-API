from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from fastapi import APIRouter, Depends, HTTPException, Response, status

from api.models import DatabaseUser, UserLogin, UserSaved
from api.utils import (
    ensure_anonymous_user,
    get_optional_user,
    get_required_user,
    verify_password,
)
from server import SETTINGS

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("", response_model=UserSaved)
def check_for_login(
    user: DatabaseUser = Depends(get_optional_user),
) -> Any:
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not logged in.",
        )

    return user


@router.post(
    "",
    response_model=UserSaved,
    dependencies=[Depends(ensure_anonymous_user)],
)
def login(
    credentials: UserLogin,
    response: Response,
) -> Any:
    try:
        user = DatabaseUser.objects.get(email=credentials.email)

        assert verify_password(
            plain_password=credentials.password,
            hashed_password=user.hashed_password,
        )

        # FIXME: Use a JWT
        response.set_cookie(key=SETTINGS.COOKIE_NAME, value=str(user.id))

        return user

    except (ObjectDoesNotExist, AssertionError) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials.",
        )


@router.delete("", response_model=None)
def logout(
    response: Response,
    user: DatabaseUser = Depends(get_required_user),
) -> Any:
    response.delete_cookie(key=SETTINGS.COOKIE_NAME)
