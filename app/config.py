import os
from functools import lru_cache

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    TELEGRAM_BOT_TOKEN: SecretStr

    TESTING = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class TestSettings(BaseSettings):
    DB_USERNAME = "admin"
    DB_PASSWORD: SecretStr = "1234"
    DB_HOST = "localhost"
    DB_PORT = 3306
    DB_NAME = "testing"

    TELEGRAM_BOT_TOKEN: SecretStr = "secret"

    TESTING = True


@lru_cache
def get_settings():
    if os.environ["APP_ENV"].lower() == "test":
        return TestSettings()
    return Settings()


settings = get_settings()
