// src/components/Navbar/Navbar.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <img src="https://as2.ftcdn.net/v2/jpg/02/78/01/07/500_F_278010790_spPoE7utG0FfoIFSMVpvF9QYmDbWSHhB.jpg" alt="Logo" />
        </Link>
        <ul className="navbar-menu">
          <li className="navbar-item">
            <Link to="/" className="navbar-link">Home</Link>
          </li>
          <li className="navbar-item">
            <Link to="/about" className="navbar-link">About</Link>
          </li>
          <li className="navbar-item">
            <Link to="/concerts" className="navbar-link">Concerts</Link>
          </li>
          <li className="navbar-item dropdown">
            <button onClick={toggleDropdown} className="navbar-link dropdown-toggle">
              More
            </button>
            {isDropdownOpen && (
              <ul className="dropdown-menu">
                <li className="dropdown-item">
                  <Link to="/login" className="dropdown-link">Login</Link>
                </li>
                <li className="dropdown-item">
                  <Link to="/register" className="dropdown-link">SignUp</Link>
                </li>
                {/* <li className="dropdown-item">
                  <Link to="/profile" className="dropdown-link">Profile</Link>
                </li> */}
              </ul>
            )}
          </li>
        </ul>
        
      </div>
    </nav>
  );
};

export default Navbar;