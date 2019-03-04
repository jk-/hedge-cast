<template>
    <v-app v-cloak>
        <Toolbar />
        <v-content>
            <router-view></router-view>
        </v-content>
        <Snackbar />
    </v-app>
</template>

<script>
    import Toolbar from '@/components/Toolbar.vue'
    import Snackbar from '@/components/Snackbar.vue'

    export default {
        name: 'App',
        components: {
            Toolbar,
            Snackbar
        }
    }
</script>
