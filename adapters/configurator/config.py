import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # settings
    PROJECT_NAME: str = "Boilerplate-fastapi"
    PROJECT_VERSION: str = "1.0.0"

    # Endpoints
    API_V1_STR: str = "/api/v1"

    # Debug mode
    DEBUG: bool = os.getenv("DEBUG", False)

    # Database
    DATABASE_URL = f"postgresql://"

    def get_database_uri() -> str:
        if settings.USE_SQLITE_DB:
            return "sqlite:///./sql_app.db"
        return settings.DATABASE_URL


settings = Settings()
