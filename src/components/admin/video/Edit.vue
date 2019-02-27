<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing Video</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
                        <AdminVideoForm :is-edit="true" />
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import AdminVideoForm from '@/components/admin/video/VideoForm.vue'

    export default {
        name: 'admin-video-edit',
        components: {
            AdminVideoForm
        }
    }
</script>
