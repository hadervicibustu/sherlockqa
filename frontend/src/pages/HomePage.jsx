import React, { useState, useEffect, useCallback } from 'react';
import { useAuth } from '../App';
import { questionsApi, ragApi } from '../services/api';
import QuestionList from '../components/Questions/QuestionList';
import QuestionForm from '../components/Questions/QuestionForm';
import Header from '../components/Common/Header';
import Modal from '../components/Common/Modal';
import Toast from '../components/Common/Toast';
import './HomePage.css';

function HomePage() {
  const { user } = useAuth();
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [toast, setToast] = useState(null);
  const [editingQuestion, setEditingQuestion] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchQuestions = useCallback(async () => {
    try {
      const response = await questionsApi.getAll(user.id);
      setQuestions(response.questions);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [user.id]);

  useEffect(() => {
    fetchQuestions();
  }, [fetchQuestions]);

  const showToast = (message, type = 'success') => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 3000);
  };

  const handleCreate = async (question, answer) => {
    try {
      const response = await questionsApi.create(user.id, question, answer);
      setQuestions((prev) => [response.question, ...prev]);
      setIsModalOpen(false);
      showToast('Question added successfully');
      return true;
    } catch (err) {
      showToast(err.message, 'error');
      return false;
    }
  };

  const handleUpdate = async (questionId, question, answer) => {
    try {
      const response = await questionsApi.update(user.id, questionId, question, answer);
      setQuestions((prev) =>
        prev.map((q) => (q.id === questionId ? response.question : q))
      );
      setEditingQuestion(null);
      setIsModalOpen(false);
      showToast('Question updated successfully');
      return true;
    } catch (err) {
      showToast(err.message, 'error');
      return false;
    }
  };

  const handleDelete = async (questionId) => {
    try {
      await questionsApi.delete(user.id, questionId);
      setQuestions((prev) => prev.filter((q) => q.id !== questionId));
      showToast('Question deleted successfully');
    } catch (err) {
      showToast(err.message, 'error');
    }
  };

  const handleAskDocuments = async (question) => {
    try {
      const response = await ragApi.query(question);
      return response.answer;
    } catch (err) {
      showToast(err.message, 'error');
      return null;
    }
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner" />
        <p>Loading your questions...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <p>Error: {error}</p>
        <button onClick={fetchQuestions}>Retry</button>
      </div>
    );
  }

  return (
    <div className="home-page">
      <Header />

      <main className="main-content">
        <div className="container">
          <div className="questions-section">
            <div className="section-header">
              <h2>Your Questions</h2>
              <div className="section-header-actions">
                <span className="question-count">{questions.length} questions</span>
                <button className="add-question-btn" onClick={() => setIsModalOpen(true)}>
                  + Add Question
                </button>
              </div>
            </div>

            <QuestionList
              questions={questions}
              onEdit={(q) => {
                setEditingQuestion(q);
                setIsModalOpen(true);
              }}
              onDelete={handleDelete}
            />
          </div>
        </div>
      </main>

      <Modal
        isOpen={isModalOpen}
        onClose={() => {
          setIsModalOpen(false);
          setEditingQuestion(null);
        }}
        title={editingQuestion ? 'Edit Question' : 'Ask a Question'}
      >
        <QuestionForm
          onSubmit={editingQuestion ? handleUpdate : handleCreate}
          onAskDocuments={handleAskDocuments}
          editingQuestion={editingQuestion}
          onCancelEdit={() => {
            setIsModalOpen(false);
            setEditingQuestion(null);
          }}
        />
      </Modal>

      {toast && (
        <Toast
          message={toast.message}
          type={toast.type}
          onClose={() => setToast(null)}
        />
      )}
    </div>
  );
}

export default HomePage;
