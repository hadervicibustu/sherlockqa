import React, { useState } from 'react';
import { useAuth } from '../App';
import { authApi } from '../services/api';
import './LoginPage.css';

function LoginPage() {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authApi.login(email);
      login(response.user);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-header">
          <div className="logo-decoration">
            <span className="decorative-symbol">&#9830;</span>
          </div>
          <h1 className="app-title">Ask Holmes</h1>
          <p className="app-subtitle">A Sherlock Holmes Knowledge Base</p>
          <div className="decorative-line">
            <span>&#8226; &#8226; &#8226;</span>
          </div>
        </div>

        <form className="login-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Enter your email to continue</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="holmes@bakerstreet.com"
              required
              disabled={loading}
              autoComplete="email"
              autoFocus
            />
          </div>

          {error && (
            <div className="error-message">
              <span className="error-icon">!</span>
              {error}
            </div>
          )}

          <button type="submit" disabled={loading || !email.trim()}>
            {loading ? (
              <>
                <span className="spinner-small" />
                Authenticating...
              </>
            ) : (
              'Enter'
            )}
          </button>
        </form>

        <div className="login-footer">
          <p className="quote">
            "When you have eliminated the impossible, whatever remains,
            however improbable, must be the truth."
          </p>
          <p className="attribution">— Sherlock Holmes</p>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
