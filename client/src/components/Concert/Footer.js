// src/components/Footer/Footer.js
import React from 'react';
import './Footer.css'; // Import the CSS file
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faFacebookF, faTwitter, faInstagram, faYoutube } from '@fortawesome/free-brands-svg-icons';
// import { faMapMarkerAlt, faPhone, faEnvelope } from '@fortawesome/free-solid-svg-icons';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section about">
          <h2 className="logo-text"><span>Concert</span>Hub</h2>
          <p>
            ConcertHub is your ultimate destination for discovering and booking tickets for the latest concerts and events. Stay connected with us for the best music experiences.
          </p>
          {/* <div className="socials">
            <a href="#">{faFacebookF} </a>
            <a href="#">{faTwitter} </a>
            <a href="#">{faInstagram} </a>
            <a href="#">{faYoutube} </a>
          </div> */}
        </div>

        <div className="footer-section links">
          <h3>Quick Links</h3>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/concerts">Concerts</a></li>

          </ul>
        </div>

        <div className="footer-section contact">
          <h3>Contact Us</h3>
          <p> Ronald Ngala Street, Nairobi City, Kenya </p>
          <p> +254 798654321</p>
          <p>info@concerthub.com</p>
        </div>
      </div>

      <div className="footer-bottom">
        &copy; 2024 ConcertHub | All Rights Reserved
      </div>
    </footer>
  );
};

export default Footer;