import Vue from 'vue'
import Vuetify from 'vuetify'
import App from '@/App.vue'
import router from '@/router'
import store from '@/store'

import 'vuetify/dist/vuetify.min.css'
require('@/sass/materialize/main.scss')
require('@/sass/index.scss')

Vue.use(Vuetify)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

Vue.filter('format_date', function (value) {
    return new Date(value*1000).toDateString()
})

Vue.filter('from_boolean', function (value) {
    return value ? 'Yes' : 'No'
})

Vue.filter('to_currency', function (value) {
    return parseFloat(value)
})

Vue.filter('or_empty', function (value) {
    return value ? value : '=empty='
})
