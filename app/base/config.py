from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: Optional[str] = "sqlite:///accounts.db"
    app_name: str = "Accounts API"
    class Config:
        case_sensitive = True

settings = Settings()