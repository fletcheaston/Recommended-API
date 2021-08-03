from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyCookie

from api.models import DatabaseUser
from server import SETTINGS

cookie_sec = APIKeyCookie(name=SETTINGS.COOKIE_NAME, auto_error=False)


def get_required_user(
    cookie_value: Optional[str] = Depends(cookie_sec),
) -> Optional[DatabaseUser]:
    if cookie_value is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not logged in.",
        )

    # FIXME: Use a JWT
    try:
        user: DatabaseUser = DatabaseUser.objects.get(id=cookie_value)
        return user
    except ObjectDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials.",
        )


def get_optional_user(
    cookie_value: Optional[str] = Depends(cookie_sec),
) -> Optional[DatabaseUser]:
    if cookie_value is None:
        return None

    # FIXME: Use a JWT
    try:
        user: DatabaseUser = DatabaseUser.objects.get(id=cookie_value)
        return user
    except ObjectDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid credentials.",
        )


def ensure_anonymous_user(
    cookie_value: Optional[str] = Depends(cookie_sec),
) -> None:
    if cookie_value is None:
        return None

    # FIXME: Use a JWT
    try:
        _ = DatabaseUser.objects.get(id=cookie_value)

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is already logged in.",
        )
    except ObjectDoesNotExist:
        return None
