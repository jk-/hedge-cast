<template>
    <v-toolbar absolute class="transparent white-text z-depth-0">
        <v-toolbar-title><router-link :to="{ name: 'index'}" class="white--text">Hedge Cast</router-link></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
            <v-btn flat v-if="isAuthenticated" class="white--text">{{ getUsername }}</v-btn>
            <v-btn flat :ripple="false" v-if="isAuthenticated" @click="logout" class="white--text">Logout</v-btn>
            <v-btn flat :ripple="false" v-if="!isAuthenticated" :to="{ name: 'login'}" class="white--text">Login</v-btn>
            <v-btn flat :ripple="false" v-if="!isAuthenticated" :to="{ name: 'register'}" class="white--text">Sign-up</v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
    export default {
        name: 'Toolbar',
        methods: {
            logout () {
                this.$store.dispatch('logout')
            }
        },
        computed: {
            getUsername () {
                return this.$store.getters.getUsername
            },
            isAuthenticated () {
                return this.$store.getters.isAuthenticated
            }
        }
    }
</script>
