<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing Role: {{ item.name }}</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
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
                                <v-btn color="erorr" @click="remove">Remove</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_role } from '@/api/index.js'
    import { save_role } from '@/api/index.js'

    export default {
        name: 'admin-role-edit',
        data () {
            return {
                item: {}
            }
        },
        methods: {
            getItem () {
                get_role(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                if (!value) {
                    value = false
                }
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
                remove_role(this.item.id).then(response => {
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
            this.getItem()
        }
    }
</script>
