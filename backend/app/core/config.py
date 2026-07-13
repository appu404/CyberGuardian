from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "CyberGuardian"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A modular cybersecurity assessment platform."
    DEBUG: bool = True


settings = Settings()
