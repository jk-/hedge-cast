<template>
    <v-app v-cloak>
        <div class="spinner text-xs-center">
            <v-progress-circular indeterminate :value="60"></v-progress-circular>
        </div>
        <v-content>
            <router-view></router-view>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        name: 'App'
    }
</script>
