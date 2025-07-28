from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator
import os

class Settings(BaseSettings):
  API_PREFIX: str = "/api"
  DEBUG: bool = False

  # Database configuration
  DB_USER: str = "postgres"
  DB_PASSWORD: str = ""
  DB_HOST: str = "localhost"
  DB_PORT: str = "5432"
  DB_NAME: str = "story_teller"
  DATABASE_URL: str = None

  # CORS configuration
  ALLOWED_HOST: str = ""

  # OpenAI API configuration
  OPENAI_API_KEY: str = ""
  OPEN_AI_API_KEY: str = ""  # Alternative naming for compatibility

  def __init__(self, **values):
    super().__init__(**values)
    
    # Use OPEN_AI_API_KEY as fallback if OPENAI_API_KEY is not set
    if not self.OPENAI_API_KEY and self.OPEN_AI_API_KEY:
      self.OPENAI_API_KEY = self.OPEN_AI_API_KEY
    
    # Construct DATABASE_URL if not provided
    if not self.DATABASE_URL:
      self.DATABASE_URL = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

  @field_validator("ALLOWED_HOST")
  def parse_allowed_host(cls, v: str) -> List[str]:
    return v.split(",") if v else []

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
    case_sensitive = True


settings = Settings()