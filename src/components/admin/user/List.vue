<template>
    <v-data-table
        :headers="headers"
        :items="users"
        class="clean-table"
        :pagination.sync="pagination"
        v-if="!loading"
      >
        <template slot="items" slot-scope="props">
        <tr @click="editUser(props.item.id)">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.username }}</td>
            <td>{{ props.item.email }}</td>
            <td>{{ props.item.created | format_date }}</td>
            <td>{{ props.item.enabled | from_boolean }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_users } from '@/api/index.js'

    export default {
        name: 'admin-users-list',

        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Username', value: 'username', sortable: false},
                    { text: 'Email', value: 'email', sortable: false},
                    { text: 'Created', value: 'created', sortable: false},
                    { text: 'Enabled', value: 'enabled', sortable: false}
                ],
                users: [],
                pagination: {
                    rowsPerPage: 25
                },
                loading: true
            }
        },
        methods: {
            getAllUsers () {
                get_all_users().then(response => {
                    this.users = response.data
                    this.loading = false
                })
            },
            editUser(id) {
                this.$router.push({ name: 'admin_user_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllUsers()
        }
    }
</script>
