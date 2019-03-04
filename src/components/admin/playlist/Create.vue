<template>
    <v-flex>
        <v-layout row>
            <v-toolbar color="transparent z-depth-0">
                <v-toolbar-title>New Playlist</v-toolbar-title>
            </v-toolbar>
        </v-layout>
        <v-container>
            <v-layout row>
                <v-flex md12>
                    <AdminPlaylistForm :is-edit="false" />
                </v-flex>
            </v-layout>
        </v-container>
    </v-flex>
</template>

<script>
    import AdminPlaylistForm from '@/components/admin/playlist/PlaylistForm.vue'

    export default {
        name: 'admin-playlist-create',
        components: {
            AdminPlaylistForm
        }
    }
</script>
