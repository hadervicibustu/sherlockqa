from flask_sqlalchemy import SQLAlchemy
from pgvector.sqlalchemy import Vector

db = SQLAlchemy()

from .user import User
from .document import Document, DocumentChunk
from .question import Question

__all__ = ["db", "User", "Document", "DocumentChunk", "Question"]
