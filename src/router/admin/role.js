
import AdminRole from '@/components/admin/role/Home.vue'
import AdminRoleEdit from '@/components/admin/role/Edit.vue'
import AdminRoleCreate from '@/components/admin/role/Create.vue'

export default [
    {
        path: 'roles',
        name: 'admin_role',
        component: AdminRole,
    },
    {
        path: 'role/edit/:id',
        name: 'admin_role_edit',
        component: AdminRoleEdit,
    },
    {
        path: 'role/create',
        name: 'admin_role_create',
        component: AdminRoleCreate,
    }
]
