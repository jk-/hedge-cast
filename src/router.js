import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import AdminHome from '@/views/admin/Home.vue'
import AdminCategory from '@/views/admin/Category.vue'
import AdminPlans from '@/views/admin/Plans.vue'
import AdminPlaylists from '@/views/admin/Playlists.vue'
import AdminRoles from '@/views/admin/Roles.vue'
import AdminVideos from '@/views/admin/Videos.vue'
import AdminUsers from '@/views/admin/Users.vue'
import AdminUsersEdit from '@/views/admin/users/Edit.vue'
import AdminCategoryEdit from '@/views/admin/category/Edit.vue'
import AdminPlanEdit from '@/views/admin/plan/Edit.vue'
import AdminPlaylistEdit from '@/views/admin/playlist/Edit.vue'
import AdminRoleEdit from '@/views/admin/role/Edit.vue'

import store from '@/store'

Vue.use(Router)

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
            requiresLogin: true
        },
        children: [
            {
                path: 'category',
                name: 'admin_category',
                component: AdminCategory,
            },
            {
                path: 'plans',
                name: 'admin_plans',
                component: AdminPlans,
            },
            {
                path: 'playlists',
                name: 'admin_playlists',
                component: AdminPlaylists,
            },
            {
                path: 'roles',
                name: 'admin_roles',
                component: AdminRoles,
            },
            {
                path: 'users',
                name: 'admin_user',
                component: AdminUsers,
            },
            {
                path: 'videos',
                name: 'admin_videos',
                component: AdminVideos,
            },
            {
                path: 'users/edit/:id',
                name: 'admin_user_edit',
                component: AdminUsersEdit,
            },
            {
                path: 'category/edit/:id',
                name: 'admin_category_edit',
                component: AdminCategoryEdit,
            },
            {
                path: 'plan/edit/:id',
                name: 'admin_plan_edit',
                component: AdminPlanEdit,
            },
            {
                path: 'playlist/edit/:id',
                name: 'admin_playlist_edit',
                component: AdminPlaylistEdit,
            },
            {
                path: 'role/edit/:id',
                name: 'admin_role_edit',
                component: AdminRoleEdit,
            }
        ]
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
