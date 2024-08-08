// src/components/Concert/ConcertDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import API from '../../api/api';

const ConcertDetails = () => {
  const { id } = useParams(); // Get the concert ID from the URL
  const [concert, setConcert] = useState(null);
  const [attendees, setAttendees] = useState([]);

  useEffect(() => {
    // Function to fetch concert details
    const fetchConcert = async () => {
      try {
        const { data } = await API.get(`/concerts/${id}`);
        setConcert(data);
      } catch (error) {
        console.error('Error fetching concert details:', error);
      }
    };

    // Function to fetch concert attendees
    const fetchAttendees = async () => {
      try {
        const { data } = await API.get(`/concerts/${id}`/attendees); // Adjust the endpoint as needed
        setAttendees(data);
      } catch (error) {
        console.error('Error fetching attendees:', error);
      }
    };

    fetchConcert();
    fetchAttendees();
  }, [id]);

  if (!concert) return <div>Loading...</div>;

  return (
    <div>
      <h1>{concert.name}</h1>
      <p>Date: {new Date(concert.date).toLocaleDateString()}</p>
      <p>Venue: {concert.venue}</p>
      {concert.image_url && <img src={concert.image_url} alt={concert.name} />}

      <h2>Attendees</h2>
      <ul>
        {attendees.length > 0 ? (
          attendees.map((attendee) => (
            <li key={attendee.id}>
              {attendee.username} ({attendee.email})
              {attendee.user_rating && <span> - Rating: {attendee.user_rating}</span>}
            </li>
          ))
        ) : (
          <li>No attendees yet</li>
        )}
      </ul>
    </div>
  );
};

export default ConcertDetails;