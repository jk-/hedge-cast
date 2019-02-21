import Vue from 'vue'
import Vuetify from 'vuetify'

import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

const files = require.context('./', true, /\.vue$/i)
files.keys().map(key => Vue.component(key.split('/').pop().split('.')[0], files(key).default))

// Vue.component('login-card', require('./components/LoginCard.vue').default);
// Vue.component('login-card', require('./components/RegisterCard.vue').default);

new Vue({
    el: '#app'
})
