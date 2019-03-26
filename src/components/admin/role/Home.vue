<template>
    <v-flex>
        <v-layout row>
            <AdminSubToolbar icon="supervised_user_circle" title="Roles" />
            <v-btn :ripple="false" :to="{name: 'admin_role_create'}">New</v-btn>
        </v-layout>
        <v-layout row>
            <v-flex md12>
                <AdminRolesList />
            </v-flex>
        </v-layout>
    </v-flex>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminRolesList from '@/components/admin/role/List.vue'

    export default {
        name: 'admin-roles',
        components: {
            AdminRolesList,
            AdminSubToolbar
        },
    }
</script>
