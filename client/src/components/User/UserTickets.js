// src/components/User/UserTickets.js
import React, { useEffect, useState } from 'react';
import API from '../../api/api';

const UserTickets = ({ userId }) => {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    const fetchTickets = async () => {
      const { data } = await API.get(`/users/${userId}`/tickets);
      setTickets(data);
    };
    fetchTickets();
  }, [userId]);

  return (
    <div>
      <h2>My Tickets</h2>
      <ul>
        {tickets.map((ticket) => (
          <li key={ticket.id}>
            Seat: {ticket.seat_number}, Price: ${ticket.price.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserTickets;