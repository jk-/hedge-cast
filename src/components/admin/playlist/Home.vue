<template>
    <v-flex>
        <v-layout row>
            <AdminSubToolbar icon="playlist_play" title="Playlist" />
            <v-btn :ripple="false" :to="{name: 'admin_playlist_create'}">New</v-btn>
        </v-layout>
        <v-layout row>
            <v-flex md12>
                <AdminPlaylistList />
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminPlaylistList from '@/components/admin/playlist/List.vue'

    export default {
        name: 'admin-category',
        components: {
            AdminPlaylistList,
            AdminSubToolbar
        },
    }
</script>
