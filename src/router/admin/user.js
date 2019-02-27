
import AdminUser from '@/components/admin/user/Home.vue'
import AdminUserEdit from '@/components/admin/user/Edit.vue'
import AdminUserCreate from '@/components/admin/user/Create.vue'


export default [
    {
        path: 'users',
        name: 'admin_user',
        component: AdminUser,
    },
    {
        path: 'user/edit/:id',
        name: 'admin_user_edit',
        component: AdminUserEdit,
    },
    {
        path: 'user/create',
        name: 'admin_user_create',
        component: AdminUserCreate,
    },
]
