"""Application configuration."""
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///app.db")
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
API_RATE_LIMIT = 100
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
SUPPORTED_FORMATS = ["json", "csv", "parquet"]
