import Vue from 'vue'
import Vuetify from 'vuetify'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'
import axios from 'axios'

import { isValidJwt } from '@/util/index.js'

import 'vuetify/dist/vuetify.min.css'
require('@/sass/materialize/main.scss')
require('@/sass/index.scss')

Vue.use(Vuetify)

Vue.config.productionTip = false

const token = localStorage.getItem('token')
if (isValidJwt(token)) {
    axios.defaults.headers.common['Authorization'] = token;
} else {
    delete axios.defaults.headers.common['Authorization']
    localStorage.setItem('token', '')
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
