import AdminPlaylist from '@/components/admin/playlist/Home.vue'
import AdminPlaylistEdit from '@/components/admin/playlist/Edit.vue'
import AdminPlaylistCreate from '@/components/admin/playlist/Create.vue'

export default [
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
]
