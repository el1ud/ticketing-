// src/api/api.js
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Update with your backend URL
});

API.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;