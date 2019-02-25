<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <AdminSubToolbar title="Videos" />
            </v-layout>
            <v-layout row>
                <v-flex md12>
                    <AdminVideosList />
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminVideosList from '@/components/admin/videos/List.vue'

    export default {
        name: 'admin-videos',
        components: {
            AdminVideosList,
            AdminSubToolbar
        },
    }
</script>
