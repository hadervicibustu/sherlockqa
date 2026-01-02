import uuid
from datetime import datetime, timezone
from pgvector.sqlalchemy import Vector
from . import db
from ..config import Config


class Document(db.Model):
    """Document model for tracking ingested PDFs."""

    __tablename__ = "documents"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String(255), nullable=False, index=True)
    title = db.Column(db.String(500))
    file_hash = db.Column(db.String(64), unique=True, nullable=False)
    indexed_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )
    chunk_count = db.Column(db.Integer, default=0)

    # Relationships
    chunks = db.relationship("DocumentChunk", backref="document", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": str(self.id),
            "filename": self.filename,
            "title": self.title,
            "file_hash": self.file_hash,
            "indexed_at": self.indexed_at.isoformat() if self.indexed_at else None,
            "chunk_count": self.chunk_count
        }


class DocumentChunk(db.Model):
    """Document chunk model for storing vectorized text segments."""

    __tablename__ = "document_chunks"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
    chunk_text = db.Column(db.Text, nullable=False)
    chunk_index = db.Column(db.Integer, nullable=False)
    embedding = db.Column(Vector(Config.EMBEDDING_DIMENSION))
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def to_dict(self):
        return {
            "id": str(self.id),
            "document_id": str(self.document_id),
            "chunk_text": self.chunk_text,
            "chunk_index": self.chunk_index,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
