<template>
    <v-app v-cloak>
        <div class="spinner text-xs-center">
            <v-progress-circular indeterminate :value="60"></v-progress-circular>
        </div>
        <v-content>
            <Toolbar />
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    import Toolbar from './components/Toolbar.vue'

    export default {
        name: 'App',
        components: {
            Toolbar
        }
    }
</script>
