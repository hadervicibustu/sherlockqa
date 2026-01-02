import React, { useState, useEffect } from 'react';
import './QuestionForm.css';

function QuestionForm({ onSubmit, onAskDocuments, editingQuestion, onCancelEdit }) {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [askingDocs, setAskingDocs] = useState(false);

  useEffect(() => {
    if (editingQuestion) {
      setQuestion(editingQuestion.question);
      setAnswer(editingQuestion.answer || '');
    } else {
      setQuestion('');
      setAnswer('');
    }
  }, [editingQuestion]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    const success = editingQuestion
      ? await onSubmit(editingQuestion.id, question, answer || null)
      : await onSubmit(question, answer || null);

    if (success) {
      setQuestion('');
      setAnswer('');
    }
    setLoading(false);
  };

  const handleAskDocuments = async () => {
    if (!question.trim()) return;

    setAskingDocs(true);
    const generatedAnswer = await onAskDocuments(question);
    if (generatedAnswer) {
      setAnswer(generatedAnswer);
    }
    setAskingDocs(false);
  };

  const handleCancel = () => {
    setQuestion('');
    setAnswer('');
    onCancelEdit();
  };

  return (
    <div className="question-form-container">
      <div className="form-header">
        <h2>{editingQuestion ? 'Edit Question' : 'Ask a Question'}</h2>
        {editingQuestion && (
          <button type="button" className="cancel-btn" onClick={handleCancel}>
            Cancel
          </button>
        )}
      </div>

      <form className="question-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="question">Question</label>
          <textarea
            id="question"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="What would you like to know about Sherlock Holmes?"
            rows={3}
            required
            disabled={loading || askingDocs}
          />
        </div>

        <div className="ask-docs-row">
          <button
            type="button"
            className="ask-docs-btn"
            onClick={handleAskDocuments}
            disabled={!question.trim() || loading || askingDocs}
          >
            {askingDocs ? (
              <>
                <span className="spinner-small" />
                Consulting the archives...
              </>
            ) : (
              <>
                <span className="docs-icon">📚</span>
                Ask Documents
              </>
            )}
          </button>
        </div>

        <div className="form-group">
          <label htmlFor="answer">Answer</label>
          <textarea
            id="answer"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Enter an answer manually or use 'Ask Documents' to generate one"
            rows={5}
            disabled={loading || askingDocs}
          />
        </div>

        <div className="form-actions">
          <button
            type="submit"
            className="submit-btn"
            disabled={!question.trim() || loading || askingDocs}
          >
            {loading ? (
              <>
                <span className="spinner-small" />
                {editingQuestion ? 'Updating...' : 'Saving...'}
              </>
            ) : (
              editingQuestion ? 'Update Question' : 'Save Question'
            )}
          </button>
        </div>
      </form>
    </div>
  );
}

export default QuestionForm;
