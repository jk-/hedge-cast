<template>
    <v-app v-cloak>
        <v-content>
            <v-container fluid fill-height>
                <v-layout align-center justify-center>
                    <router-view></router-view>
                </v-layout>
            </v-container>
        </v-content>
        <Snackbar />
    </v-app>
</template>

<script>
    import Snackbar from '@/components/Snackbar.vue'

    export default {
        name: 'SimpleLayout',
        components: {
            Snackbar
        }
    }
</script>
