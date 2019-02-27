<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <AdminSubToolbar title="Category" />
            </v-layout>
            <v-layout row>
                <v-flex md12>
                    <AdminCategoryList />
                </v-flex>
            </v-layout>
            <v-layout row>
                <v-flex>
                    <v-btn :to="{name: 'admin_category_create'}">Create Category</v-btn>
                </v-flex>
            </v-layout>
        </v-flex>
    </v-layout>
</template>

<script>

    import AdminSubToolbar from '@/components/admin/SubToolbar.vue'
    import AdminCategoryList from '@/components/admin/category/List.vue'

    export default {
        name: 'admin-category',
        components: {
            AdminCategoryList,
            AdminSubToolbar
        },
    }
</script>
