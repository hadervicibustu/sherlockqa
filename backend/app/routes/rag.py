from flask import Blueprint, request, jsonify
from ..services import RAGService

rag_bp = Blueprint("rag", __name__)


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
