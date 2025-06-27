# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cached_property

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
                               

    model_config = SettingsConfigDict(          # replaces old inner Config
        env_file=".env",                        # read vars from .env
        extra="ignore",                         # ignore unknown env vars
    )

    @cached_property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()   # type: ignore