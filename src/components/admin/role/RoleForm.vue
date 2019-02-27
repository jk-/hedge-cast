<template>
    <v-form>
        <v-flex md4>
            <v-text-field
                label="Name"
                :value="item.name"
                @input="update('name', $event)"
            >
            </v-text-field>
        </v-flex>
        <v-flex md4>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="erorr" @click="remove">Remove</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import { get_role } from '@/api/index.js'
    import { save_role } from '@/api/index.js'
    import { delete_role } from '@/api/index.js'

    export default {
        name: 'admin-role-edit',
        props: ['isEdit'],
        data () {
            return {
                item: {},
                editing: this.isEdit
            }
        },
        methods: {
            getItem () {
                get_role(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                this.$set(this.item, param, value)
            },
            save () {
                save_role(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated role"
                    }
                    this.$router.push({name: 'admin_role'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            },
            remove () {
                delete_role(this.item.id).then(response => {
                    this.item = response.data
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$router.push({name: 'admin_role'})
                    this.$store.dispatch('setSnackbar', payload)

                })
            }
        },
        created () {
            if (this.editing)
                this.getItem()
        }
    }
</script>
