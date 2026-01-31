from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://postgres:jrLRdIuFFqCivTsLeyBVZUxPkylOWzZq@maglev.proxy.rlwy.net:14388/railway"

    class Config:
        env_file = ".env"
        case_sensitive = True

# singleton
settings = Settings()