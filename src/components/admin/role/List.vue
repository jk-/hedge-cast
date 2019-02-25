<template>
    <v-data-table
        :headers="headers"
        :items="items"
        class="clean-table"
        :pagination.sync="pagination"
      >
        <template slot="items" slot-scope="props">
        <tr @click="edit(props.item.id)">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_roles } from '@/api/index.js'

    export default {
        name: 'admin-roles-list',

        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Name', value: 'name', sortable: false}
                ],
                items: [],
                pagination: {
                    rowsPerPage: 25
                }
            }
        },
        methods: {
            getAllItems () {
                get_all_roles().then(response => {
                    this.items = response.data
                })
            },
            edit(id) {
                this.$router.push({ name: 'admin_role_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllItems()
        }
    }
</script>
