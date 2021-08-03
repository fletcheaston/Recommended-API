from typing import Any

from django.db.utils import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, Response, status

from api.models import DatabaseUser, UserCreate, UserSaved
from api.utils import ensure_anonymous_user, get_password_hash, get_required_user
from server import SETTINGS

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "", response_model=UserSaved, dependencies=[Depends(ensure_anonymous_user)]
)
def create_user(
    user_data: UserCreate,
    response: Response,
) -> Any:
    try:
        user = DatabaseUser.objects.create(
            name=user_data.name,
            email=user_data.email,
            hashed_password=get_password_hash(user_data.password),
        )

        # FIXME: Use a JWT
        response.set_cookie(key=SETTINGS.COOKIE_NAME, value=str(user.id))

        return user

    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists.",
        )


@router.delete("", response_model=None)
def delete_my_user_account(
    response: Response,
    user: DatabaseUser = Depends(get_required_user),
) -> Any:
    response.delete_cookie(key=SETTINGS.COOKIE_NAME)

    user.delete()
