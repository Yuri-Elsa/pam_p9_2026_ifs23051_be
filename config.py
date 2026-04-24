import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey_change_in_prod")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///recipes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt_secret_change_in_prod")
    JWT_ACCESS_TOKEN_EXPIRES = False  # No expiry for simplicity

    LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://delcom.org/api")
    LLM_TOKEN = os.environ.get("LLM_TOKEN", "YOUR_TOKEN_HERE")
    LLM_MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
