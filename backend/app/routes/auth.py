from flask import Blueprint, request, jsonify
from ..services import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    """Authenticate user by email."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Request body is required"}), 400

        email = data.get("email")

        user, error = AuthService.authenticate_by_email(email)

        if error:
            return jsonify({"error": error}), 401

        return jsonify({
            "message": "Authentication successful",
            "user": user.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user (admin endpoint)."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    email = data.get("email")

    user, error = AuthService.create_user(email)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "message": "User registered successfully",
        "user": user.to_dict()
    }), 201


@auth_bp.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    """Get user by ID."""
    user = AuthService.get_user_by_id(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": user.to_dict()}), 200
