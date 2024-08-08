// src/components/User/UserProfile.js
import React, { useEffect, useState } from 'react';
import API from '../../api/api';

const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      const { data } = await API.get(`/users/${userId}`);
      setUser(data);
    };
    fetchUser();
  }, [userId]);

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>{user.username}</h1>
      <p>Email: {user.email}</p>
      <h2>Tickets</h2>
      {/* Add logic to display user's tickets */}
    </div>
  );
};

export default UserProfile;