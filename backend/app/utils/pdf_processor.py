import hashlib
import os
import re
from PyPDF2 import PdfReader
from ..config import Config


class PDFProcessor:
    """Utility for processing PDF documents into chunks."""

    def __init__(
        self,
        chunk_size: int = Config.CHUNK_SIZE,
        chunk_overlap: int = Config.CHUNK_OVERLAP
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def extract_text(self, pdf_path: str) -> str:
        """Extract all text from a PDF file."""
        reader = PdfReader(pdf_path)
        text_parts = []

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)

        return "\n".join(text_parts)

    def clean_text(self, text: str) -> str:
        """Clean extracted text by removing extra whitespace."""
        # Replace multiple whitespace with single space
        text = re.sub(r"\s+", " ", text)
        # Remove leading/trailing whitespace
        text = text.strip()
        return text

    def chunk_text(self, text: str) -> list[str]:
        """Split text into overlapping chunks."""
        text = self.clean_text(text)

        if len(text) <= self.chunk_size:
            return [text] if text else []

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size

            # Try to break at sentence boundary if possible
            if end < len(text):
                # Look for sentence endings within the last 100 characters
                search_start = max(end - 100, start)
                last_period = text.rfind(".", search_start, end)
                last_question = text.rfind("?", search_start, end)
                last_exclaim = text.rfind("!", search_start, end)

                best_break = max(last_period, last_question, last_exclaim)
                if best_break > start:
                    end = best_break + 1

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            # Move start position with overlap
            start = end - self.chunk_overlap

        return chunks

    def calculate_file_hash(self, pdf_path: str) -> str:
        """Calculate SHA-256 hash of a PDF file."""
        sha256_hash = hashlib.sha256()

        with open(pdf_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()

    def process_pdf(self, pdf_path: str) -> dict:
        """Process a PDF file and return metadata with chunks."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        filename = os.path.basename(pdf_path)
        file_hash = self.calculate_file_hash(pdf_path)
        text = self.extract_text(pdf_path)
        chunks = self.chunk_text(text)

        # Try to extract title from filename
        title = os.path.splitext(filename)[0].replace("_", " ").replace("-", " ").title()

        return {
            "filename": filename,
            "title": title,
            "file_hash": file_hash,
            "chunks": chunks,
            "chunk_count": len(chunks)
        }
