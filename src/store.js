import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.config.devtools = true

Vue.use(Vuex)

import { authenticate, register } from '@/api/index.js'
import { isValidJwt, EventBus, getJwtUsername } from '@/util/index.js'

const token = localStorage.getItem('token')

const state = {
    userData: {
        username: getJwtUsername(token)
    },
    jwt: token,
    snackbar: {
        visible: false,
        color: '',
        timeout: 2000,
        text: ''
    }
}

const actions = {
    login (context, userData) {
        return authenticate(userData)
            .then(response =>  {
                context.commit('setJwtToken', { jwt: response.data })
                context.commit('setUserData', { userData })
                EventBus.$emit('successAuthentication')
            })
            .catch(error => {
                context.commit('setJwtToken')
                context.commit('setUserData')
                EventBus.$emit('failedAuthentication', error)
        })
    },
    logout (context) {
        context.commit('setJwtToken')
        context.commit('setUserData')
        router.push({ name: 'index' })
    },
    register (context, userData) {
        context.commit('setUserData', { userData })
        return register(userData)
            .then(context.dispatch('login', userData))
            .catch(error => {
                EventBus.$emit('failedRegistering: ', error)
        })
    },
    setSnackbar (context, payload) {
        context.commit('showSnackbar', payload)
    }
}

const mutations = {
    setUserData (state, payload) {
        if (payload) {
            state.userData = payload.userData
        } else {
            state.userData = {}
        }
    },
    setJwtToken (state, payload) {
        if (payload) {
            localStorage.setItem('token', payload.jwt.token)
            state.jwt = payload.jwt.token
        } else {
            localStorage.setItem('token', '')
            state.jwt = ''
            delete axios.defaults.headers.common['Authorization']
        }
    },
    showSnackbar(state, payload) {
        console.log(payload)
        state.snackbar.text = payload.text
        state.snackbar.visible = true
        state.snackbar.color = payload.color
    },
    closeSnackbar(state) {
        state.snackbar.visible = false
        state.snackbar.text = null
    },
}

const getters = {
    isAuthenticated (state) {
        return isValidJwt(state.jwt) && !!localStorage.getItem('token')
    },
    getUsername (state) {
        return state.userData.username
    }
}

export default new Vuex.Store({
    state,
    actions,
    mutations,
    getters,
})

Vue.config.devtools = true
