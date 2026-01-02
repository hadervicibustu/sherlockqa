import React from 'react';
import QuestionItem from './QuestionItem';
import './QuestionList.css';

function QuestionList({ questions, onEdit, onDelete }) {
  if (questions.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">&#9830;</div>
        <h3>No questions yet</h3>
        <p>
          Begin your investigation by asking a question about Sherlock Holmes novels.
          Use "Ask Documents" to receive answers from the archives.
        </p>
      </div>
    );
  }

  return (
    <div className="question-list">
      {questions.map((question) => (
        <QuestionItem
          key={question.id}
          question={question}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}

export default QuestionList;
