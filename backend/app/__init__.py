from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import RequestEntityTooLarge
from .config import Config
from .models import db


def create_app():
    """Application factory for creating Flask app."""
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
    app.config["MAX_CONTENT_LENGTH"] = Config.MAX_UPLOAD_SIZE

    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.questions import questions_bp
    from .routes.rag import rag_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(questions_bp, url_prefix="/api/questions")
    app.register_blueprint(rag_bp, url_prefix="/api/rag")

    @app.errorhandler(RequestEntityTooLarge)
    def handle_file_too_large(e):
        max_size_mb = Config.MAX_UPLOAD_SIZE / (1024 * 1024)
        return jsonify({
            "error": f"File too large. Maximum size is {max_size_mb:.1f}MB"
        }), 413

    # Create tables
    with app.app_context():
        # Enable pgvector extension
        db.session.execute(db.text("CREATE EXTENSION IF NOT EXISTS vector"))
        db.session.commit()
        db.create_all()

    return app
