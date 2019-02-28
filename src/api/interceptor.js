import axios from 'axios'
import store from '@/store'
import router from '@/router'
import { isValidJwt } from '@/util/index.js'

axios.interceptors.request.use(
  (config) => {
    var token = localStorage.getItem('token')
    if (isValidJwt(token)) {
      config.headers['Authorization'] = 'Bearer ' + token
    }
    config.headers['X-Requested-With'] = 'XMLHttpRequest'
    config.headers['Accept-Language'] = 'en'
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

axios.interceptors.response.use(
    (response) => {
        if (response.data.message !== 'undefined' && response.data.message) {
            let payload = {
                color: response.data.type,
                text: response.data.message
            }
            store.dispatch('setSnackbar', payload)
        }
        return response
    },
    (error) => {
        if (error.response === "undefined") {
            let payload = {
               color: 'error',
               text: 'Network Error.'
            }
            store.dispatch('setSnackbar', payload)
            router.push({ name: 'index' })
            return Promise.reject(error)
       } else if (error.response.status === 401) {
            let payload = {
                color: 'error',
                text: error.response.data.error.message[0]
            }
            store.dispatch('setSnackbar', payload)
            if (error.response.data.error.type === 'AuthRequired') {
                store.dispatch('logout', payload)
            }
       } else {
            let payload = {
                color: 'error',
                text: error.response.data.error.message[0]
            }
            store.dispatch('setSnackbar', payload)
        }
        return Promise.reject(error)
    }
)
