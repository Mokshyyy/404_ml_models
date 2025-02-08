import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Flask backend URL
  withCredentials: true, // Important for CORS to allow cookies
});

export default api;
