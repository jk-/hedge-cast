
import AdminCategory from '@/components/admin/category/Home.vue'
import AdminCategoryEdit from '@/components/admin/category/Edit.vue'
import AdminCategoryCreate from '@/components/admin/category/Create.vue'

export default [
    {
        path: 'category',
        name: 'admin_category',
        component: AdminCategory
    },
    {
        path: 'category/edit/:id',
        name: 'admin_category_edit',
        component: AdminCategoryEdit
    },
    {
        path: 'category/create',
        name: 'admin_category_create',
        component: AdminCategoryCreate
    }
]
