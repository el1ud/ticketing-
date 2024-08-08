// src/pages/Home.js
import React from 'react';
import ConcertList from './Concert/ConcertList';
import Footer from './Concert/Footer';

const Home = () => (
  <div>
    <h1>Welcome to the Concert Ticket App</h1>
    <ConcertList />
    <Footer />
  </div>
);

export default Home;