import React from "react";
import "./Footer.css";
import "@fortawesome/fontawesome-free/css/all.min.css"; // ✅ Import Font Awesome

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section links">
            <ul>
              <li>
                <a href="/" aria-label="Home">
                  Home
                </a>
              </li>
              <li>
                <a href="/rent" aria-label="Rent">
                  Rent
                </a>
              </li>
              <li>
                <a href="/buy" aria-label="Buy">
                  Buy
                </a>
              </li>
            </ul>
          </div>
          <div className="footer-section social">
            <div className="social-icons">
              <a
                href="https://facebook.com"
                aria-label="Facebook"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fab fa-facebook-f"></i>
              </a>
              <a
                href="https://instagram.com"
                aria-label="Instagram"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fab fa-instagram"></i>
              </a>
              <a
                href="https://twitter.com"
                aria-label="Twitter"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fab fa-twitter"></i>
              </a>
              <a
                href="https://linkedin.com"
                aria-label="LinkedIn"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fab fa-linkedin-in"></i>
              </a>
              <a
                href="https://youtube.com"
                aria-label="YouTube"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fab fa-youtube"></i>
              </a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {currentYear} GharKhoj. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
