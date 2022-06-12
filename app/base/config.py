'''
Provides the settings for the Accounts API
'''
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    '''
    The settings object contains settings for
    the Accounts API app
    :param BaseSettings: takes in pyndantic base settings
    '''
    SQLALCHEMY_DATABASE_URL: Optional[str] = "sqlite:///accounts.db"
    app_name: str = "Accounts API"
    class Config:
        case_sensitive = True

settings = Settings()