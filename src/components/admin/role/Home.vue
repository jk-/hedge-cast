<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <AdminSubToolbar title="Roles" />
            </v-layout>
            <v-layout row>
                <v-flex md12>
                    <AdminRolesList />
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
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
