<template>
    <v-data-table
        :headers="headers"
        :items="items"
        class="clean-table"
        :pagination.sync="pagination"
        v-if="!loading"
      >
        <template slot="items" slot-scope="props">
        <tr @click="editCategory(props.item.id)">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_categories } from '@/api/index.js'

    export default {
        name: 'admin-users-list',
        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Name', value: 'name', sortable: false}
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
                get_all_categories().then(response => {
                    this.items = response.data
                    this.loading = false
                })
            },
            editCategory(id) {
                this.$router.push({ name: 'admin_category_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllItems()
        }
    }
</script>
