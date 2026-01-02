import React from 'react';
import './Toast.css';

function Toast({ message, type = 'success', onClose }) {
  return (
    <div className={`toast toast-${type}`} onClick={onClose}>
      <span className="toast-icon">
        {type === 'success' ? '✓' : '!'}
      </span>
      <span className="toast-message">{message}</span>
    </div>
  );
}

export default Toast;
