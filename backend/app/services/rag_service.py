import os
from ..models import db, Document, DocumentChunk
from ..utils import EmbeddingModel, PDFProcessor, LLMClient
from ..config import Config


class RAGService:
    """Service for RAG operations."""

    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.embedding_model = EmbeddingModel()
        self.llm_client = LLMClient()

    def index_document(self, pdf_path: str) -> tuple[Document | None, str | None]:
        """
        Index a PDF document into the vector store.
        Returns (document, None) on success, (None, error_message) on failure.
        """
        try:
            # Process PDF
            pdf_data = self.pdf_processor.process_pdf(pdf_path)

            # Check if document already exists
            existing = Document.query.filter_by(file_hash=pdf_data["file_hash"]).first()
            if existing:
                return None, f"Document already indexed: {existing.filename}"

            # Create document record
            document = Document(
                filename=pdf_data["filename"],
                title=pdf_data["title"],
                file_hash=pdf_data["file_hash"],
                chunk_count=pdf_data["chunk_count"]
            )
            db.session.add(document)
            db.session.flush()

            # Generate embeddings for all chunks
            embeddings = self.embedding_model.embed_batch(pdf_data["chunks"])

            # Create chunk records
            for i, (chunk_text, embedding) in enumerate(zip(pdf_data["chunks"], embeddings)):
                chunk = DocumentChunk(
                    document_id=document.id,
                    chunk_text=chunk_text,
                    chunk_index=i,
                    embedding=embedding
                )
                db.session.add(chunk)

            db.session.commit()
            return document, None

        except FileNotFoundError as e:
            return None, str(e)
        except Exception as e:
            db.session.rollback()
            return None, f"Error indexing document: {str(e)}"

    def index_all_documents(self) -> tuple[list[dict], list[dict]]:
        """
        Index all PDF documents in the books folder.
        Returns (successes, failures) lists.
        """
        books_folder = Config.BOOKS_FOLDER
        successes = []
        failures = []

        if not os.path.exists(books_folder):
            os.makedirs(books_folder)
            return successes, [{"filename": "books folder", "error": "Folder was empty, created now"}]

        pdf_files = [f for f in os.listdir(books_folder) if f.lower().endswith(".pdf")]

        if not pdf_files:
            return successes, [{"filename": "books folder", "error": "No PDF files found"}]

        for pdf_file in pdf_files:
            pdf_path = os.path.join(books_folder, pdf_file)
            document, error = self.index_document(pdf_path)

            if document:
                successes.append({
                    "filename": document.filename,
                    "title": document.title,
                    "chunk_count": document.chunk_count
                })
            else:
                failures.append({
                    "filename": pdf_file,
                    "error": error
                })

        return successes, failures

    def search_similar_chunks(
        self,
        query: str,
        top_k: int = Config.TOP_K_RESULTS
    ) -> list[DocumentChunk]:
        """Search for the most similar document chunks to a query."""
        # Generate query embedding
        query_embedding = self.embedding_model.embed(query)

        # Perform vector similarity search using pgvector
        chunks = DocumentChunk.query.order_by(
            DocumentChunk.embedding.cosine_distance(query_embedding)
        ).limit(top_k).all()

        return chunks

    def generate_answer(self, question: str) -> tuple[str | None, str | None]:
        """
        Generate an answer for a question using RAG.
        Returns (answer, None) on success, (None, error_message) on failure.
        """
        try:
            # Search for relevant chunks
            chunks = self.search_similar_chunks(question)

            if not chunks:
                return None, "No relevant documents found. Please index some documents first."

            # Extract chunk texts
            context_texts = [chunk.chunk_text for chunk in chunks]

            # Generate answer using LLM
            answer = self.llm_client.generate_answer(question, context_texts)

            return answer, None

        except Exception as e:
            return None, f"Error generating answer: {str(e)}"

    def get_indexed_documents(self) -> list[Document]:
        """Get all indexed documents."""
        return Document.query.order_by(Document.indexed_at.desc()).all()

    def delete_document(self, document_id: str) -> tuple[bool, str | None]:
        """Delete a document and its chunks."""
        document = Document.query.get(document_id)

        if not document:
            return False, "Document not found"

        try:
            db.session.delete(document)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)
