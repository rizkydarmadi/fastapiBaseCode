from sqlalchemy.orm import Session
import models
from schemas import movies_schemas
from schemas import users_schemas
from datetime import datetime
from sqlalchemy import delete


class UserRepository:
    @staticmethod
    def create_user(db: Session, _user: users_schemas.UserRequest):
        db_user = models.User(
            email=_user.email,
            username=_user.user_name,
            password=_user.password,
            is_active=True,
            created_at=datetime.now(),
            updated_at=None,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return (
            db.query(models.User)
            .filter(models.User.is_active == True, models.User.deleted_at == None)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_user(db: Session, id: int):
        return db.query(models.User).filter(models.User.id == id).first()

    @staticmethod
    def update_user(db: Session, _user: users_schemas.UserRequest, id: int):
        user_object: models.User = (
            db.query(models.User).filter(models.User.id == id).first()
        )

        user_object.username = _user.user_name
        user_object.password = _user.password
        user_object.email = _user.email
        user_object.updated_at = datetime.now()

        db.add(user_object)
        db.commit()
        db.refresh(user_object)
        return user_object

    # soft delete
    @staticmethod
    def delete_movie(db: Session, id: int):
        db.query(models.Movie).filter(models.Movie.id == id).delete()
        db.commit()
