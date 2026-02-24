from pydantic_settings import BaseSettings , SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):

  PROJECT_NAME: str = "Estate Auction Analyzer"


  EDEVLET_BASE_URL: str
  EDEVLET_PAGE_STEP: int = 20
  EDEVLET_MAX_SF: int = 140
  TKGM_URL: str
  GEMINI_API_KEY: Optional[str] = None

  model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()