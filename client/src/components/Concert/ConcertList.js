// src/components/Concert/ConcertList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ConcertList.css'; // Import the CSS file for styling
import Footer from './Footer';

const ConcertList = () => {
  const [concerts, setConcerts] = useState([]);

  useEffect(() => {
    const fetchConcerts = async () => {
      try {
        const { data } = await axios.get('http://127.0.0.1:5000/api/concerts');
        setConcerts(data);
      } catch (error) {
        console.error('Error fetching concerts:', error);
      }
    };
    fetchConcerts();
  }, []);

  return (
    <div className="concert-list">
      <h1>Upcoming Concerts</h1>
      <div className="concert-grid">
        {concerts.map((concert) => (
          <div key={concert.id} className="concert-card">
            <img src={concert.image_url} alt={concert.name} className="concert-image" />
            <div className="concert-details">
              <h2 className="concert-name">{concert.name}</h2>
              <p className="concert-venue">{concert.venue}</p>
              <p className="concert-date">{concert.date}</p>
            </div>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default ConcertList;