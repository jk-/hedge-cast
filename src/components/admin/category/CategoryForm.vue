<template>
    <v-form>
        <v-flex md9>
            <v-text-field
                label="Name"
                :value="item.name"
                @input="update('name', $event)"
            >
            </v-text-field>
        </v-flex>
        <v-flex md4>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="isEdit" color="error" @click="remove">Delete</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import { get_category } from '@/api/index.js'
    import { save_category } from '@/api/index.js'
    import { delete_category } from '@/api/index.js'

    export default {
        name: 'admin-category-form',
        props: {
            isEdit: Boolean
        },
        data () {
            return {
                item: {},
                editor: this.isEdit
            }
        },
        methods: {
            getCategory () {
                get_category(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                this.$set(this.item, param, value)
            },
            save () {
                save_category(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated item"
                    }
                    this.$store.dispatch('setSnackbar', payload)
                    this.$router.push({name: 'admin_category'})
                })
            },
            remove () {
                delete_category(this.item.id).then(response => {
                    this.item = {}
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$store.dispatch('setSnackbar', payload)
                    this.$router.push({name: 'admin_category'})
                })
            }
        },
        created () {
            if (this.editor)
                this.getCategory()
        }
    }

</script>
