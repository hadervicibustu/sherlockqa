import React from 'react';
import { useAuth } from '../../App';
import './Header.css';

function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="app-header">
      <div className="container header-content">
        <div className="header-brand">
          <span className="brand-symbol">&#9830;</span>
          <h1 className="brand-title">Ask Holmes</h1>
        </div>

        <div className="header-user">
          <span className="user-email">{user.email}</span>
          <button className="logout-btn" onClick={logout}>
            Sign Out
          </button>
        </div>
      </div>
    </header>
  );
}

export default Header;
