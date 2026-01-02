from flask import Flask
from flask_cors import CORS
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

    # Create tables
    with app.app_context():
        # Enable pgvector extension
        db.session.execute(db.text("CREATE EXTENSION IF NOT EXISTS vector"))
        db.session.commit()
        db.create_all()

    return app
