<template>
    <v-flex>
        <v-layout row>
            <v-toolbar color="transparent z-depth-0">
                <v-toolbar-title>New Category</v-toolbar-title>
            </v-toolbar>
        </v-layout>
        <v-container>
            <v-layout row>
                <v-flex md12>
                    <AdminCategoryForm :is-edit="false"/>
                </v-flex>
            </v-layout>
        </v-container>
    </v-flex>
</template>

<script>
    import AdminCategoryForm from '@/components/admin/category/CategoryForm.vue'

    export default {
        name: 'admin-category-create',
        components: {
            AdminCategoryForm
        }
    }
</script>
