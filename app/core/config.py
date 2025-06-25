# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str                           # snake-case field

    model_config = SettingsConfigDict(          # replaces old inner Config
        env_file=".env",                        # read vars from .env
        extra="ignore",                         # ignore unknown env vars
    )

settings = Settings()   # type: ignore