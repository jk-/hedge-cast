<template>
    <v-flex>
        <v-layout row>
            <AdminSubToolbar icon="videocam" title="Videos" />
            <v-btn :ripple="false" :to="{name: 'admin_video_create'}">New</v-btn>
        </v-layout>
        <v-layout row>
            <v-flex md12>
                <AdminVideosList />
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminVideosList from '@/components/admin/video/List.vue'

    export default {
        name: 'admin-video',
        components: {
            AdminVideosList,
            AdminSubToolbar
        },
    }
</script>
