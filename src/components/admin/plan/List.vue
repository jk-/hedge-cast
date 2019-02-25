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
            <td>{{ props.item.code }}</td>
            <td>{{ props.item.price | to_currency }}</td>
        </tr>
        </template>
    </v-data-table>
</template>

<script>

    import { get_all_plans } from '@/api/index.js'

    export default {
        name: 'admin-plan-list',

        data () {
            return {
                headers: [
                    { text: 'ID', value: 'id', sortable: false, width: 3},
                    { text: 'Name', value: 'name', sortable: false},
                    { text: 'Code', value: 'code', sortable: false},
                    { text: 'Price', value: 'price', sortable: false}
                ],
                items: [],
                pagination: {
                    rowsPerPage: 25
                }
            }
        },
        methods: {
            getAllItems () {
                get_all_plans().then(response => {
                    this.items = response.data
                })
            },
            edit(id) {
                this.$router.push({ name: 'admin_plan_edit', params: { id: id } })
            }
        },
        mounted () {
            this.getAllItems()
        }
    }
</script>
