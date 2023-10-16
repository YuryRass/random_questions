"""Модуль для настройки проекта"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Конфигурационные данные"""
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    URL: str

    @property
    def DATABASE_URL(self):
        """URL адрес для подключения к БД PostgreSQL"""
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@" + \
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
