
import AdminVideo from '@/components/admin/video/Home.vue'
import AdminVideoEdit from '@/components/admin/video/Edit.vue'
import AdminVideoCreate from '@/components/admin/video/Create.vue'

export default [
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
    }
]
