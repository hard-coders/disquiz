from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url = "sqlite:///./dis_quiz.db"
