import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration."""

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/sherlock"
    )

    # Anthropic API
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

    # RAG Configuration
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    TOP_K_RESULTS = 3

    # Embedding model
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    EMBEDDING_DIMENSION = 384

    # Books folder path
    BOOKS_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "books")

    # Upload settings
    MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB max file size
