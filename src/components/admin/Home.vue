<template>
    <v-layout row fill-height>
        <Navigation/>
        <router-view></router-view>
    </v-layout>
</template>

<script>
    import Navigation from '@/components/admin/Navigation.vue'

    export default {
        components: {
            Navigation
        }
    }
</script>
