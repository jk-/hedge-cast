import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App.vue'
import router from './router'

import 'vuetify/dist/vuetify.min.css'
require('./sass/materialize/main.scss')
require('./sass/index.scss')

Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
