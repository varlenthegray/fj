from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm.session import Session
from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.db.session import SessionLocal
from app.models.author import Author


class TokenData(BaseModel):
    id: Optional[int] = None


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None

    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> Author:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM], options={"verify_aud": False})
        author_id: int = payload.get("sub")

        if author_id is None:
            raise credentials_exception

        token_data = TokenData(id=author_id)
    except JWTError:
        raise credentials_exception

    user = db.query(Author).filter(Author.id == token_data.id).first()

    if user is None:
        raise credentials_exception

    return user
