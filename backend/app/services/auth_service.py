from ..models import db, User


class AuthService:
    """Service for authentication operations."""

    @staticmethod
    def authenticate_by_email(email: str) -> tuple[User | None, str | None]:
        """
        Authenticate user by email.
        Returns (user, None) on success, (None, error_message) on failure.
        """
        if not email or not email.strip():
            return None, "Email is required"

        email = email.strip().lower()

        # Validate email format
        if "@" not in email or "." not in email:
            return None, "Invalid email format"

        # Look up user
        user = User.query.filter_by(email=email).first()

        if not user:
            return None, "User not registered. Please contact administrator."

        return user, None

    @staticmethod
    def get_user_by_id(user_id: str) -> User | None:
        """Get user by ID."""
        try:
            return User.query.get(user_id)
        except Exception:
            return None

    @staticmethod
    def create_user(email: str) -> tuple[User | None, str | None]:
        """
        Create a new user (admin function).
        Returns (user, None) on success, (None, error_message) on failure.
        """
        if not email or not email.strip():
            return None, "Email is required"

        email = email.strip().lower()

        # Check if user already exists
        existing = User.query.filter_by(email=email).first()
        if existing:
            return None, "User already exists"

        try:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
            return user, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)
