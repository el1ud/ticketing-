// src/components/About.js
import React from 'react';
import Footer from '../Concert/Footer';

const About = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>About Us</h1>
      <p style={styles.text}>
        Welcome to our Concert Ticketing Platform! We are passionate about bringing the best live music experiences to fans worldwide. Our platform provides a seamless way to explore and purchase tickets for concerts, offering a wide range of artists and genres.
      </p>
      <p style={styles.text}>
        Our team is dedicated to ensuring a smooth and enjoyable experience, from discovering upcoming events to securing your seat. We work closely with artists, venues, and fans to create unforgettable live music experiences.
      </p>
      <p style={styles.text}>
        Whether you're a die-hard fan or just looking for a great night out, we've got you covered. Thank you for choosing us to be a part of your musical journey.
      </p>
      {/* <p style={styles.text}>
        If you have any questions or need assistance, please don't hesitate to <a href="/contact" style={styles.link}>contact us</a>. We are here to help you every step of the way!
      </p> */}
      <Footer />
    </div>
  );
};

// Styles
const styles = {
  container: {
    padding: '20px',
    maxWidth: '800px',
    margin: '0 auto',
    textAlign: 'center',
  },
  title: {
    fontSize: '2.5em',
    marginBottom: '20px',
  },
  text: {
    fontSize: '1.2em',
    marginBottom: '15px',
    lineHeight: '1.6',
  },
  link: {
    color: '#007bff',
    textDecoration: 'none',
  },
};

export default About;