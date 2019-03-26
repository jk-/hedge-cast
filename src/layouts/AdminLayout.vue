<template>
    <v-app class="white" v-cloak>
        <Navigation />
        <v-toolbar app absolute flat>
          <v-toolbar-side-icon
            @click.stop="primaryDrawer.model = !primaryDrawer.model"
          ></v-toolbar-side-icon>
          <v-toolbar-title>Hedge Cast</v-toolbar-title>
        </v-toolbar>
        <v-content fluid fill-height>
            <router-view></router-view>
        </v-content>
        <Snackbar />
    </v-app>
</template>

<script>
    import Navigation from '@/components/admin/Navigation.vue'
    import Snackbar from '@/components/Snackbar.vue'

    export default {
        name: 'AdminLayout',
        components: {
            Snackbar,
            Navigation
        }
    }
</script>
