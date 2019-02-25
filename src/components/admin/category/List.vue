<template>
    <v-data-table
        :headers="headers"
        :items="categories"
        class="clean-table"
        :pagination.sync="pagination"
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
                categories: [],
                pagination: {
                    rowsPerPage: 25
                }
            }
        },
        methods: {
            getAllCategories () {
                get_all_categories().then(response => {
                    this.categories = response.data
                })
            },
            editCategory(id) {
                this.$router.push({ name: 'admin_category_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllCategories()
        }
    }
</script>
