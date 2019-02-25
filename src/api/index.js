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
  return axios.put(`${API_URL}/user`, user)
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

/*
 Plan
*/
export function get_all_plans() {
  return axios.get(`${API_URL}/plans`)
}

export function get_plan(id) {
  return axios.get(`${API_URL}/plan/${id}`)
}

/*
 Playlist
*/
export function get_all_playlists() {
  return axios.get(`${API_URL}/playlists`)
}

export function get_playlist(id) {
  return axios.get(`${API_URL}/playlist/${id}`)
}

/*
 Roles
*/
export function get_all_roles() {
  return axios.get(`${API_URL}/roles`)
}

export function get_role(id) {
  return axios.get(`${API_URL}/role/${id}`)
}

/*
 Videos
*/
export function get_all_videos() {
  return axios.get(`${API_URL}/videos`)
}

export function get_video(id) {
  return axios.get(`${API_URL}/video/${id}`)
}
