import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import "../styles/Navbar.css"; // Assuming styles are in the src folder

const Navbar = ({ user, setUser }) => {
  const [showModal, setShowModal] = useState(false);
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");
  const [isSignup, setIsSignup] = useState(false); // State for toggling between Login and Signup

  const handleLogin = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setMessage(data.message);

    if (response.status === 200) {
      setUser({ username: formData.username }); // Set user after successful login
      setTimeout(() => {
        setShowModal(false);
      }, 1500);
    } else {
      // Handle login failure (401 Unauthorized)
      setMessage("Invalid username or password");
    }
  };

  const handleSignup = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setMessage(data.message);

    if (response.status === 200) {
      // Automatically switch to the login form after successful signup
      setIsSignup(false);
      setTimeout(() => {
        setShowModal(false);
      }, 1500);
    }
  };

  return (
    <nav className="navbar">
      <div className="logo">
        <h1>GharKhoj</h1>
      </div>
      <ul className="nav-links">
        <li><a href="/">Home</a></li>
        <li><a href="/rent">Rent</a></li>
        <li><a href="/buy">Buy</a></li>
        <li><a href="/sell">Sell</a></li>
      </ul>
      <div className="login">
        {user ? (
          <span>Welcome, {user.username}</span>
        ) : (
          <FontAwesomeIcon icon={faUser} className="login-icon" onClick={() => setShowModal(true)} />
        )}
      </div>

      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <button className="close-modal" onClick={() => setShowModal(false)}>
              &times;
            </button>
            <h2>{isSignup ? "Sign Up" : "Login"}</h2>
            <form onSubmit={isSignup ? handleSignup : handleLogin}>
              <input
                type="text"
                placeholder="Username"
                value={formData.username}
                onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                required
              />
              <input
                type="password"
                placeholder="Password"
                value={formData.password}
                onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                required
              />
              <button type="submit">{isSignup ? "Sign Up" : "Login"}</button>
            </form>
            <p>{message}</p>
            <p>
              {isSignup ? (
                <span onClick={() => setIsSignup(false)} style={{ cursor: 'pointer' }}>Already have an account? Login</span>
              ) : (
                <span onClick={() => setIsSignup(true)} style={{ cursor: 'pointer' }}>Don't have an account? Sign Up</span>
              )}
            </p>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
