from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET: str = "Dffk4fY7t6Yzd3OMV2/YXyxZ04eNfzQ7w9QkIfT2MqA="
    ALGORITHM: str = "HS256"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:3000', 'http://127.0.0.1:3000']

    # SQLAlchemy database setup
    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///database.db"

    # First (admin) superuser
    FIRST_SUPERUSER: str = "bbeach"
    FIRST_SUPERUSER_PW: str = "Yellow"  # todo: remove this and pull it from a .env file or something
    FIRST_SUPERUSER_EMAIL: EmailStr = "bbeach@innovated.tech"
    FIRST_SUPERUSER_PEN_NAME: str = "Ben Beach"

    class Config:
        case_sensitive = True


settings = Settings()
