<template>
    <v-flex>
        <v-layout row>
            <AdminSubToolbar icon="folder" title="Category" />
            <v-btn :ripple="false" :to="{name: 'admin_category_create'}">New</v-btn>
        </v-layout>
        <v-layout row>
            <v-flex md12>
                <AdminCategoryList />
            </v-flex>
        </v-layout>
    </v-flex>
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
