from pydantic import BaseSettings


class Settings(BaseSettings):
    # API
    PORT: int = 8000
    CONN_DB: str | None = None

    # Platzi
    PLATZI_URL: str = "https://platzi.com"

    class Config:
        env_file = '.env'