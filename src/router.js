import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/login/Home.vue'
import Register from '@/components/register/Home.vue'
import AdminHome from '@/components/admin/Home.vue'

import AdminCategory from '@/components/admin/category/Home.vue'
import AdminCategoryEdit from '@/components/admin/category/Edit.vue'
import AdminCategoryCreate from '@/components/admin/category/Create.vue'

import AdminPlan from '@/components/admin/plan/Home.vue'
import AdminPlanEdit from '@/components/admin/plan/Edit.vue'
import AdminPlanCreate from '@/components/admin/plan/Create.vue'

import AdminRole from '@/components/admin/role/Home.vue'
import AdminRoleEdit from '@/components/admin/role/Edit.vue'
import AdminRoleCreate from '@/components/admin/role/Create.vue'

import AdminVideo from '@/components/admin/video/Home.vue'
import AdminVideoEdit from '@/components/admin/video/Edit.vue'
import AdminVideoCreate from '@/components/admin/video/Create.vue'

import AdminUser from '@/components/admin/user/Home.vue'
import AdminUserEdit from '@/components/admin/user/Edit.vue'
import AdminUserCreate from '@/components/admin/user/Create.vue'

import AdminPlaylist from '@/components/admin/playlist/Home.vue'
import AdminPlaylistEdit from '@/components/admin/playlist/Edit.vue'
import AdminPlaylistCreate from '@/components/admin/playlist/Create.vue'

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
                path: 'category/edit/:id',
                name: 'admin_category_edit',
                component: AdminCategoryEdit
            },
            {
                path: 'category/create',
                name: 'admin_category_create',
                component: AdminCategoryCreate
            },

            {
                path: 'plans',
                name: 'admin_plan',
                component: AdminPlan,
            },
            {
                path: 'plan/edit/:id',
                name: 'admin_plan_edit',
                component: AdminPlanEdit,
            },

            {
                path: 'users',
                name: 'admin_user',
                component: AdminUser,
            },
            {
                path: 'users/edit/:id',
                name: 'admin_user_edit',
                component: AdminUserEdit,
            },
            {
                path: 'users/create',
                name: 'admin_user_create',
                component: AdminUserCreate,
            },


            {
                path: 'videos',
                name: 'admin_video',
                component: AdminVideo,
            },
            {
                path: 'video/edit/:id',
                name: 'admin_video_edit',
                component: AdminVideoEdit,
            },
            {
                path: 'video/create',
                name: 'admin_video_create',
                component: AdminVideoCreate,
            },


            {
                path: 'playlists',
                name: 'admin_playlist',
                component: AdminPlaylist,
            },
            {
                path: 'playlist/edit/:id',
                name: 'admin_playlist_edit',
                component: AdminPlaylistEdit,
            },
            {
                path: 'playlist/create',
                name: 'admin_playlist_create',
                component: AdminPlaylistCreate,
            },

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
            },
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
