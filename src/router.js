import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/login/Home.vue'
import Register from '@/components/register/Home.vue'
import AdminHome from '@/components/admin/Home.vue'

import AdminDashboard from '@/components/admin/Dashboard.vue'
import AdminCategoryRoutes from '@/router/admin/category'
import AdminPlanRoutes from '@/router/admin/plan'
import AdminPlaylistRoutes from '@/router/admin/playlist'
import AdminRoleRoutes from '@/router/admin/role'
import AdminUserRoutes from '@/router/admin/user'
import AdminVideoRoutes from '@/router/admin/video'

import store from '@/store'

const ROLE_ADMIN = "ROLE_ADMIN"
const APP_TITLE = "Hedge Cast"
const LAYOUTS = {
    APP: 'app-layout',
    ADMIN: 'admin-layout',
    SIMPLE: 'simple-layout'
}

Vue.use(Router)

let admin_routes = [
    {
        path: '',
        name: 'admin_dashboard',
        component: AdminDashboard
    }
]
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
        component: Home,
        meta: {
            title: APP_TITLE,
            layout: LAYOUTS.APP
        }
    },
    {
        path: '/login',
        name: 'login',
        component: Login,
        meta: {
            title: APP_TITLE + ' Login',
            layout: LAYOUTS.SIMPLE
        }
    },
    {
        path: '/register',
        name: 'register',
        component: Register,
        meta: {
            title: APP_TITLE + ' Register',
            layout: LAYOUTS.SIMPLE
        }
    },
    {
        path: '/admin',
        name: 'admin_home',
        component: AdminHome,
        meta: {
            requiresLogin: true,
            requiresRole: ROLE_ADMIN,
            layout: LAYOUTS.ADMIN
        },
        children: admin_routes
    },
  ]
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresLogin) && !store.getters.isAuthenticated) {
        store.commit('setLayout', LAYOUTS.SIMPLE)
        next("login")
    } else {
        const layout = to.matched.slice().reverse().find(r => r.meta && r.meta.layout);
        if (layout.meta.layout) store.commit('setLayout', layout.meta.layout)
        next()
    }

    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
    if(nearestWithTitle) document.title = nearestWithTitle.meta.title;


})

export default router
