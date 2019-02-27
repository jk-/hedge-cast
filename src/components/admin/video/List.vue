<template>
    <v-data-table
        :headers="headers"
        :items="items"
        class="clean-table"
        :pagination.sync="pagination"
        v-if="!loading"
      >
        <template slot="items" slot-scope="props">
        <tr @click="edit(props.item.id)">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.title }}</td>
            <td>{{ props.item.created | format_date }}</td>
            <td>{{ props.item.access_type }}</td>
            <td>{{ props.item.enabled | from_boolean }}</td>
            <td>{{ props.item.url }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_videos } from '@/api/index.js'

    export default {
        name: 'admin-video-list',

        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Title', value: 'title', sortable: false},
                    { text: 'Created', value: 'created', sortable: false},
                    { text: 'Access Type', value: 'access_type', sortable: false},
                    { text: 'Enabled', value: 'enabled', sortable: false},
                    { text: 'URL', value: 'url', sortable: false}
                ],
                items: [],
                pagination: {
                    rowsPerPage: 25
                },
                loading: true
            }
        },
        methods: {
            getAllItems () {
                get_all_videos().then(response => {
                    this.items = response.data
                    this.loading = false
                })
            },
            edit(id) {
                this.$router.push({ name: 'admin_video_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllItems()
        }
    }
</script>
