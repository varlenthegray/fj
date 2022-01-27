from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorUpdate
from app.core.security import get_password_hash


class CRUDAuthor(CRUDBase[Author, AuthorCreate, AuthorUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[Author]:
        return db.query(Author).filter(Author.username == username).first()

    def get_by_email(self, db: Session, *, email: str) -> Optional[Author]:
        return db.query(Author).filter(Author.email_address == email).first()

    def create(self, db: Session, *, obj_in: AuthorCreate) -> Author:
        create_data = obj_in.dict()
        create_data.pop("password")
        db_obj = Author(**create_data)
        db_obj.hashed_password = get_password_hash(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

    def update(self, db: Session, *, db_obj: Author, obj_in: Union[AuthorUpdate, Dict[str, Any]]) -> Author:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def is_admin(self, author: Author) -> bool:
        return author.admin


author = CRUDAuthor(Author)
