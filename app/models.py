from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.main import get_settings

settings = get_settings()

engine = create_engine(settings.db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
Base.metadata.create_all(bind=engine)


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(
        DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp()
    )


class User(Base, BaseMixin):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
