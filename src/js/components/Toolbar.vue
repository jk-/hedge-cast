<template>
    <v-toolbar class="transparent z-depth-0">
        <v-toolbar-side-icon></v-toolbar-side-icon>
        <v-toolbar-title><router-link :to="{ name: 'index'}" class="black-text">Hedge Cast</router-link></v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
            <v-btn flat><router-link :to="{ name: 'login'}" class="black-text">Login</router-link></v-btn>
            <v-btn flat><router-link :to="{ name: 'register'}" class="black-text">Sign-up</router-link></v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
    export default {
        name: 'Toolbar'
    }
</script>
