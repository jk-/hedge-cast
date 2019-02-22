import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import { authenticate, register } from './api/index.js'
import { isValidJwt, EventBus } from './util/index.js'

const state = {
    userData: {},
    jwt: ''
}

const actions = {
    login (context, userData) {
    context.commit('setUserData', { userData })
    return authenticate(userData)
        .then(response => context.commit('setJwtToken', { jwt: response.data }))
        .catch(error => {
            console.log('Error Authenticating: ', error.message)
            EventBus.$emit('failedAuthentication', error.message)
        })
    },
    register (context, userData) {
        context.commit('setUserData', { userData })
        return register(userData)
            .then(context.dispatch('login', userData))
            .catch(error => {
                console.log('Error Registering: ', error)
                EventBus.$emit('failedRegistering: ', error)
        })
    },
}

const mutations = {
    setUserData (state, payload) {
        console.log('setUserData payload = ', payload)
        state.userData = payload.userData
    },
    setJwtToken (state, payload) {
        console.log('setJwtToken payload = ', payload)
        localStorage.token = payload.jwt.token
        state.jwt = payload.jwt
    }
}

const getters = {
    isAuthenticated (state) {
        return isValidJwt(state.jwt.token)
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
