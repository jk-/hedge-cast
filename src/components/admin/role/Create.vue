<template>
    <v-flex>
        <v-layout row>
            <v-toolbar color="transparent z-depth-0">
                <v-toolbar-title>New Role</v-toolbar-title>
            </v-toolbar>
        </v-layout>
        <v-container>
            <v-layout row>
                <v-flex md12>
                    <AdminRoleForm :is-edit="false" />
                </v-flex>
            </v-layout>
        </v-container>
    </v-flex>
</template>

<script>
    import AdminRoleForm from '@/components/admin/role/RoleForm.vue'

    export default {
        name: 'admin-role-create',
        components: {
            AdminRoleForm
        }
    }
</script>
