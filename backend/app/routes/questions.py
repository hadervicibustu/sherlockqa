from flask import Blueprint, request, jsonify
from ..services import QuestionService

questions_bp = Blueprint("questions", __name__)


def get_user_id_from_request():
    """Extract user ID from request headers."""
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        return None
    return user_id


@questions_bp.route("", methods=["GET"])
def get_questions():
    """Get all questions for the authenticated user."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    questions = QuestionService.get_user_questions(user_id)

    return jsonify({
        "questions": [q.to_dict() for q in questions]
    }), 200


@questions_bp.route("/<question_id>", methods=["GET"])
def get_question(question_id):
    """Get a specific question by ID."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    question = QuestionService.get_question_by_id(question_id, user_id)

    if not question:
        return jsonify({"error": "Question not found"}), 404

    return jsonify({"question": question.to_dict()}), 200


@questions_bp.route("", methods=["POST"])
def create_question():
    """Create a new question."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    question_text = data.get("question")
    answer = data.get("answer")

    question, error = QuestionService.create_question(user_id, question_text, answer)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Question created successfully",
        "question": question.to_dict()
    }), 201


@questions_bp.route("/<question_id>", methods=["PUT"])
def update_question(question_id):
    """Update an existing question."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    question_text = data.get("question")
    answer = data.get("answer")

    question, error = QuestionService.update_question(
        question_id, user_id, question_text, answer
    )

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "Question updated successfully",
        "question": question.to_dict()
    }), 200


@questions_bp.route("/<question_id>", methods=["DELETE"])
def delete_question(question_id):
    """Delete a question."""
    user_id = get_user_id_from_request()

    if not user_id:
        return jsonify({"error": "User ID is required in X-User-ID header"}), 401

    success, error = QuestionService.delete_question(question_id, user_id)

    if not success:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Question deleted successfully"}), 200
