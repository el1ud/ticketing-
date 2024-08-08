// src/components/Concert/ConcertItem.js
import React from 'react';
import { Link } from 'react-router-dom';

const ConcertItem = ({ concert }) => (
  <div>
    <h2>{concert.name}</h2>
    <p>Date: {new Date(concert.date).toLocaleDateString()}</p>
    <p>Venue: {concert.venue}</p>
    <Link to={`/concerts/${concert.id}`}>View Details</Link>
  </div>
);

export default ConcertItem;