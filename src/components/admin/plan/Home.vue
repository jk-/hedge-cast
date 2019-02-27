<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <AdminSubToolbar title="Plans" />
                <v-btn :ripple="false" :to="{name: 'admin_plan_create'}">New</v-btn>
            </v-layout>
            <v-layout row>
                <v-flex md12>
                    <AdminPlanList />
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminPlanList from '@/components/admin/plan/List.vue'

    export default {
        name: 'admin-plans',
        components: {
            AdminSubToolbar,
            AdminPlanList
        },
    }
</script>
