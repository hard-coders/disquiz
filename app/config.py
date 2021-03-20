from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url = "sqlite:///./dis_quiz.db"


@lru_cache()
def get_settings():
    return Settings()
