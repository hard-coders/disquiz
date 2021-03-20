from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.api.dependencies import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.User])
def get_user_list(session: Session = Depends(get_db)):
    return session.query(models.User).all()


@router.post("", response_model=schemas.ResponseId)
def create_user(user: schemas.UserCreate, session: Session = Depends(get_db)):
    user = models.User(
        email=user.email,
        username=user.username,
        hashed_password=user.password,
    )
    session.add(user)
    session.commit()

    return user
