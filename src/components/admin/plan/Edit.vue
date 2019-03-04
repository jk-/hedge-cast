<template>
    <v-flex>
        <v-layout row>
            <v-toolbar color="transparent z-depth-0">
                <v-toolbar-title>Editing Plan</v-toolbar-title>
            </v-toolbar>
        </v-layout>
        <v-container>
            <v-layout row>
                <v-flex md12>
                    <AdminPlanForm :is-edit="true" />
                </v-flex>
            </v-layout>
        </v-container>
    </v-flex>
</template>

<script>
    import AdminPlanForm from '@/components/admin/plan/PlanForm.vue'

    export default {
        name: 'admin-plan-edit',
        components: {
            AdminPlanForm
        }
    }
</script>
