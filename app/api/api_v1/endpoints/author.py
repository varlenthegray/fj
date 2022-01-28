from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app import crud
from app import schemas
from app.api import deps
from app.core.auth import (authenticate, create_access_token)
from app.models.author import Author

router = APIRouter()


@router.post("/login", summary="Log in")
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """

    user = authenticate(username=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": create_access_token(sub=str(user.id)), "token_type": "bearer"}


@router.get("/me", response_model=schemas.Author, summary="Get current user")
def read_users_me(current_user: Author = Depends(deps.get_current_user)):
    """
    Fetch the current logged in user.
    """

    user = current_user

    return user


@router.post("/signup", response_model=schemas.Author, status_code=201, summary="Sign up for a new account")
def create_user_signup(*, db: Session = Depends(deps.get_db), user_in: schemas.author.AuthorCreate) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = db.query(Author).filter(Author.username == user_in.username).first()

    if user:
        raise HTTPException(status_code=400, detail="A user with this username already exists in the system")

    user = crud.user.create(db=db, obj_in=user_in)

    return user


@router.post("/create_moderator", response_model=schemas.Author, status_code=201, summary="Create a moderator")  # include_in_schema=False when release
def create_moderator(
        *,
        db: Session = Depends(deps.get_db),
        current_user: Author = Depends(deps.get_current_user),
        user_in: schemas.author.AuthorCreateModerator
) -> Any:
    """
    Create a moderator when a superuser is logged in. This is called from an administrator account.
    """

    user = db.query(Author).filter(Author.username == user_in.username).first()

    if user:
        raise HTTPException(status_code=400, detail="A user with this username already exists in the system")

    if not current_user.admin:
        raise HTTPException(status_code=403, detail="You do not have sufficient privileges to create a moderator")
    else:
        user = crud.author.create(db=db, obj_in=user_in)

    return user
