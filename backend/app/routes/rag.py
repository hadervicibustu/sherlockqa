import os
import shutil
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from ..services import RAGService
from ..config import Config

rag_bp = Blueprint("rag", __name__)

ALLOWED_EXTENSIONS = {'.pdf'}


def get_user_id_from_request():
    """Extract user ID from request headers."""
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        return None
    return user_id


def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return os.path.splitext(filename.lower())[1] in ALLOWED_EXTENSIONS


def is_valid_pdf(file_stream):
    """Check if the file content is actually a PDF by verifying magic bytes."""
    file_stream.seek(0)  # Ensure we're at the start before reading
    header = file_stream.read(4)
    file_stream.seek(0)  # Reset stream position for later use
    return header == b'%PDF'


@rag_bp.route("/upload", methods=["POST"])
def upload_book():
    """Upload a PDF book to the books folder."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    if not is_valid_pdf(file.stream):
        return jsonify({"error": "File content is not a valid PDF"}), 400

    filename = secure_filename(file.filename)

    if not filename:
        return jsonify({"error": "Invalid filename"}), 400

    os.makedirs(Config.BOOKS_FOLDER, exist_ok=True)

    filepath = os.path.join(Config.BOOKS_FOLDER, filename)

    try:
        fd = os.open(filepath, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return jsonify({"error": f"File '{filename}' already exists"}), 409
    except OSError as e:
        return jsonify({"error": f"Failed to create file: {e.strerror}"}), 500

    try:
        with os.fdopen(fd, 'wb') as f:
            file.stream.seek(0)
            shutil.copyfileobj(file.stream, f)
    except OSError as e:
        os.unlink(filepath)
        return jsonify({"error": f"Failed to save file: {e.strerror}"}), 500

    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename
    }), 201


@rag_bp.route("/index", methods=["POST"])
def index_documents():
    """Index all PDF documents in the books folder."""
    rag_service = RAGService()

    successes, failures = rag_service.index_all_documents()

    return jsonify({
        "message": "Document indexing completed",
        "indexed": successes,
        "failed": failures,
        "total_indexed": len(successes),
        "total_failed": len(failures)
    }), 200


@rag_bp.route("/query", methods=["POST"])
def query_documents():
    """Query documents and generate an answer."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    question = data.get("question")

    if not question or not question.strip():
        return jsonify({"error": "Question is required"}), 400

    rag_service = RAGService()
    answer, error = rag_service.generate_answer(question.strip())

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "question": question,
        "answer": answer
    }), 200


@rag_bp.route("/documents", methods=["GET"])
def get_documents():
    """Get all indexed documents."""
    rag_service = RAGService()
    documents = rag_service.get_indexed_documents()

    return jsonify({
        "documents": [doc.to_dict() for doc in documents]
    }), 200


@rag_bp.route("/documents/<document_id>", methods=["DELETE"])
def delete_document(document_id):
    """Delete an indexed document."""
    rag_service = RAGService()
    success, error = rag_service.delete_document(document_id)

    if not success:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Document deleted successfully"}), 200


@rag_bp.route("/search", methods=["POST"])
def search_chunks():
    """Search for relevant document chunks without generating an answer."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    query = data.get("query")
    top_k = data.get("top_k", 3)

    if not query or not query.strip():
        return jsonify({"error": "Query is required"}), 400

    rag_service = RAGService()
    chunks = rag_service.search_similar_chunks(query.strip(), top_k)

    return jsonify({
        "query": query,
        "chunks": [chunk.to_dict() for chunk in chunks]
    }), 200
