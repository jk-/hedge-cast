import axios from 'axios'
import { isValidJwt } from '@/util/index.js'

const token = localStorage.getItem('token')

if (isValidJwt(token)) {
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + token;
} else {
    delete axios.defaults.headers.common['Authorization']
    localStorage.removeItem('token')
}

const API_URL = 'http://127.0.0.1:5000/api'

export function authenticate(userData) {
  return axios.post(`${API_URL}/login`, userData)
}

export function register(userData) {
  return axios.post(`${API_URL}/register`, userData)
}

/*
 USERS
*/
export function get_all_users() {
  return axios.get(`${API_URL}/users`)
}

export function get_user(id) {
  return axios.get(`${API_URL}/user/${id}`)
}

export function save_user(user) {
  return axios.post(`${API_URL}/user`, user)
}

/*
 Categories
*/
export function get_all_categories() {
  return axios.get(`${API_URL}/categories`)
}

export function get_category(id) {
  return axios.get(`${API_URL}/category/${id}`)
}
