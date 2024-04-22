from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DB_URI: str
    FASTAPI_PRODUCTION: bool = False


settings = Settings()
