from datetime import datetime, timezone
from ..models import db, Question


class QuestionService:
    """Service for question CRUD operations."""

    @staticmethod
    def get_user_questions(user_id: str) -> list[Question]:
        """Get all questions for a user, ordered by creation date descending."""
        return Question.query.filter_by(user_id=user_id).order_by(
            Question.created_at.desc()
        ).all()

    @staticmethod
    def get_question_by_id(question_id: str, user_id: str) -> Question | None:
        """Get a specific question by ID, ensuring it belongs to the user."""
        return Question.query.filter_by(id=question_id, user_id=user_id).first()

    @staticmethod
    def create_question(
        user_id: str,
        question: str,
        answer: str | None = None
    ) -> tuple[Question | None, str | None]:
        """
        Create a new question.
        Returns (question, None) on success, (None, error_message) on failure.
        """
        if not question or not question.strip():
            return None, "Question text is required"

        try:
            new_question = Question(
                user_id=user_id,
                question=question.strip(),
                answer=answer.strip() if answer else None
            )
            db.session.add(new_question)
            db.session.commit()
            return new_question, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def update_question(
        question_id: str,
        user_id: str,
        question_text: str | None = None,
        answer: str | None = None
    ) -> tuple[Question | None, str | None]:
        """
        Update an existing question.
        Returns (question, None) on success, (None, error_message) on failure.
        """
        existing = Question.query.filter_by(id=question_id, user_id=user_id).first()

        if not existing:
            return None, "Question not found"

        try:
            if question_text is not None:
                existing.question = question_text.strip()
            if answer is not None:
                existing.answer = answer.strip() if answer else None

            existing.updated_at = datetime.now(timezone.utc)
            db.session.commit()
            return existing, None
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def delete_question(question_id: str, user_id: str) -> tuple[bool, str | None]:
        """
        Delete a question.
        Returns (True, None) on success, (False, error_message) on failure.
        """
        existing = Question.query.filter_by(id=question_id, user_id=user_id).first()

        if not existing:
            return False, "Question not found"

        try:
            db.session.delete(existing)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)
