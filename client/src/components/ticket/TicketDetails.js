// src/components/Ticket/TicketDetails.js
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import API from '../../../api/api';

const TicketDetails = () => {
  const { id } = useParams();
  const [ticket, setTicket] = useState(null);

  useEffect(() => {
    const fetchTicket = async () => {
      const { data } = await API.get(`/tickets/${id}`);
      setTicket(data);
    };
    fetchTicket();
  }, [id]);

  if (!ticket) return <div>Loading...</div>;

  return (
    <div>
      <h1>Ticket Details</h1>
      <p>Seat Number: {ticket.seat_number}</p>
      <p>Price: ${ticket.price.toFixed(2)}</p>
      <p>Concert: {ticket.concert_id}</p>
      <p>User: {ticket.user_id}</p>
    </div>
  );
};

export default TicketDetails;