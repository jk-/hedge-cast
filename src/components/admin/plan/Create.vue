<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>New Plan</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
                        <AdminPlanForm :is-edit="false" />
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import AdminPlanForm from '@/components/admin/plan/PlanForm.vue'

    export default {
        name: 'admin-plan-create',
        components: {
            AdminPlanForm
        }
    }
</script>
