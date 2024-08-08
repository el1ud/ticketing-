// src/components/Auth/Login.js
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import API from '../../api/api';
import './Login.css';

const Login = ({ setToken }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await API.post('/login', { email, password });
      // localStorage.setItem('token', data.access_token);
      // setToken(data.access_token);
      history.push('/');
    } catch (err) {
      console.error('Invalid credentials', err);
    }
  };

  return (

    <div className='Container-login'>
      <form onSubmit={handleSubmit}>
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit">Login</button>
    </form>
    </div>
   
  );
};

export default Login;