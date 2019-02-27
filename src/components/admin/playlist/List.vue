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
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.enabled | trom_boolean }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_playlists } from '@/api/index.js'

    export default {
        name: 'admin-playlist-list',

        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Name', value: 'name', sortable: false},
                    { text: 'Enabled', value: 'enabled', sortable: false}
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
                get_all_playlists().then(response => {
                    this.items = response.data
                    this.loading = false
                })
            },
            edit(id) {
                this.$router.push({ name: 'admin_playlist_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllItems()
        }
    }
</script>
