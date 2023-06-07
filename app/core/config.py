from pydantic import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    CONN_DB: str | None = None
    RELOAD: bool = False

    # Platzi
    PLATZI_URL: str = "https://platzi.com"

     # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = 'HS256'
    JWT_EXPIRATION_TIME_MINUTES: int = 3600

    class Config:
        env_file = '.env'