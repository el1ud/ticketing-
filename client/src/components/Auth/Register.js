// src/components/Auth/Register.js
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import API from '../../api/api';
import axios from 'axios';
import './Register.css'; // Import the CSS file

const Register = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await axios.post('http://127.0.0.1:5000/register', { username, email, password });
      // localStorage.setItem('token', data.access_token);
      // setToken(data.access_token);
      history.push('/');
    } catch (err) {
      console.error('Registration error', err);
    }
  };

  return (
    <div className='register-body'>
       <form className="register-form" onSubmit={handleSubmit}>
      <input
        className="register-input"
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        className="register-input"
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        className="register-input"
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button className="register-button" type="submit">Register</button>
    </form>
    </div>

  );
};

export default Register;