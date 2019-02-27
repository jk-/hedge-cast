
import AdminPlan from '@/components/admin/plan/Home.vue'
import AdminPlanEdit from '@/components/admin/plan/Edit.vue'
import AdminPlanCreate from '@/components/admin/plan/Create.vue'

export default [
    {
        path: 'plans',
        name: 'admin_plan',
        component: AdminPlan,
    },
    {
        path: 'plan/edit',
        name: 'admin_plan_edit',
        component: AdminPlanEdit,
    },
    {
        path: 'plan/create',
        name: 'admin_plan_create',
        component: AdminPlanCreate,
    },
]
