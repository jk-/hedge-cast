import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/login/Home.vue'
import Register from '@/components/register/Home.vue'
import AdminHome from '@/components/admin/Home.vue'

import AdminCategoryRoutes from '@/router/admin/category'
import AdminPlanRoutes from '@/router/admin/plan'
import AdminPlaylistRoutes from '@/router/admin/playlist'
import AdminRoleRoutes from '@/router/admin/role'
import AdminUserRoutes from '@/router/admin/user'
import AdminVideoRoutes from '@/router/admin/video'

import store from '@/store'

Vue.use(Router)


let admin_routes = []
admin_routes = admin_routes.concat(
    AdminCategoryRoutes, AdminPlanRoutes, AdminPlaylistRoutes,
    AdminRoleRoutes, AdminUserRoutes, AdminVideoRoutes
)

const router = new Router({
  mode: 'history',
  routes: [
    {
        path: '/',
        name: 'index',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/register',
        name: 'register',
        component: Register
    },
    {
        path: '/admin',
        name: 'admin_home',
        component: AdminHome,
        meta: {
            requiresLogin: true,
            requiresRole: "ROLE_ADMIN"
        },
        children: admin_routes
    },
  ]
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin) && !store.getters.isAuthenticated) {
        next("login")
    } else {
        next()
    }
})

export default router
