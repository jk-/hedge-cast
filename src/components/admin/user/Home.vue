<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <AdminSubToolbar title="Users" />
                <v-btn :ripple="false" :to="{name: 'admin_user_create'}">New</v-btn>
            </v-layout>
            <v-layout row>
                <v-flex md12>
                    <AdminUserList />
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminUserList from '@/components/admin/user/List.vue'

    export default {
        name: 'admin-users',
        components: {
            AdminUserList,
            AdminSubToolbar
        },
    }
</script>
