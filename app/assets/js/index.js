import Vue from 'vue'
import Vuetify from 'vuetify'

import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

Vue.component('login-card', require('./components/LoginCard.vue').default);

new Vue({
    el: '#app'
})
