import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import { authenticate, register } from '@/api/index.js'
import { isValidJwt, EventBus, getJwtUsername } from '@/util/index.js'

const token = localStorage.getItem('token')

const state = {
    userData: {
        username: getJwtUsername(token)
    },
    jwt: token
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
                context.commit('setJwtToken', {})
                context.commit('setUserData', {})
                EventBus.$emit('failedAuthentication', error)
        })
    },
    logout () {
        context.commit('setJwtToken', {})
        context.commit('setUserData', {})
    },
    register (context, userData) {
        context.commit('setUserData', { userData })
        return register(userData)
            .then(context.dispatch('login', userData))
            .catch(error => {
                EventBus.$emit('failedRegistering: ', error)
        })
    },
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
        }
    }
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
