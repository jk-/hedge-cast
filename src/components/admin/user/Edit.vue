<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing User</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
                        <AdminUserForm :is-edit="true" />
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import AdminUserForm from '@/components/admin/user/UserForm.vue'

    export default {
        name: 'admin-user-edit',
        components: {
            AdminUserForm
        }
    }
</script>
