from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Blog Post Backend"

    DB_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"


settings: Settings = Settings()  # type: ignore
