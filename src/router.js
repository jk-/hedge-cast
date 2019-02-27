import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/login/Home.vue'
import Register from '@/components/register/Home.vue'
import AdminHome from '@/components/admin/Home.vue'
import AdminCategory from '@/components/admin/category/Home.vue'
import AdminPlans from '@/components/admin/plan/Home.vue'
import AdminPlaylists from '@/components/admin/playlist/Home.vue'
import AdminRoles from '@/components/admin/role/Home.vue'
import AdminVideos from '@/components/admin/video/Home.vue'
import AdminUsers from '@/components/admin/user/Home.vue'
import AdminUsersEdit from '@/components/admin/user/Edit.vue'
import AdminCategoryEdit from '@/components/admin/category/Edit.vue'
import AdminPlanEdit from '@/components/admin/plan/Edit.vue'
import AdminPlaylistEdit from '@/components/admin/playlist/Edit.vue'
import AdminRoleEdit from '@/components/admin/role/Edit.vue'
import AdminVideosEdit from '@/components/admin/video/Edit.vue'
import AdminCategoryCreate from '@/components/admin/category/Create.vue'

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
                component: AdminCategory
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
            },
            {
                path: 'video/edit/:id',
                name: 'admin_video_edit',
                component: AdminVideosEdit,
            },
            {
                path: 'category/create',
                name: 'admin_category_create',
                component: AdminCategoryCreate,
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
