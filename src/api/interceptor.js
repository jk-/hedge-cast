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
      return response
    },
    (error) => {
        let payload = {
            color: 'error',
            text: error.response.data.message
        }
        store.dispatch('setSnackbar', payload)
        if (error.response.status === 401) {
            store.dispatch('logout').then(() => {
                router.push({ name: 'login' })
            }).catch(() => {
                router.push({ name: 'login' })
            })
        }
        return Promise.reject(error)
    }
)
