import React, { useState, useRef, useEffect } from 'react';
import './QuestionItem.css';

function QuestionItem({ question, onEdit, onDelete }) {
  const [menuOpen, setMenuOpen] = useState(false);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const menuRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (menuRef.current && !menuRef.current.contains(event.target)) {
        setMenuOpen(false);
        setConfirmDelete(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleEdit = () => {
    setMenuOpen(false);
    onEdit(question);
  };

  const handleDeleteClick = () => {
    if (confirmDelete) {
      onDelete(question.id);
      setMenuOpen(false);
      setConfirmDelete(false);
    } else {
      setConfirmDelete(true);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
    });
  };

  return (
    <div className="question-item">
      <div className="question-content">
        <div className="question-header">
          <span className="question-date">{formatDate(question.created_at)}</span>
          <div className="menu-container" ref={menuRef}>
            <button
              className="menu-trigger"
              onClick={() => setMenuOpen(!menuOpen)}
              aria-label="Question options"
            >
              <span className="menu-dots">⋮</span>
            </button>

            {menuOpen && (
              <div className="menu-dropdown">
                <button className="menu-item" onClick={handleEdit}>
                  <span className="menu-icon">✎</span>
                  Edit
                </button>
                <button
                  className={`menu-item menu-item-danger ${confirmDelete ? 'confirm' : ''}`}
                  onClick={handleDeleteClick}
                >
                  <span className="menu-icon">✕</span>
                  {confirmDelete ? 'Confirm Delete' : 'Delete'}
                </button>
              </div>
            )}
          </div>
        </div>

        <p className="question-text">{question.question}</p>

        <div className="answer-section">
          {question.answer ? (
            <p className="answer-text">
              {question.answer.length > 200
                ? `${question.answer.substring(0, 200)}...`
                : question.answer}
            </p>
          ) : (
            <p className="no-answer">Not answered</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default QuestionItem;
