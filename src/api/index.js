import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000'

export function authenticate (userData) {
  return axios.post(`${API_URL}/user/login`, userData)
}

export function register (userData) {
  return axios.post(`${API_URL}/user/register`, userData)
}
