<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>New Category</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
                        <v-form>
                            <v-flex md4>
                                <v-text-field
                                    label="Name"
                                    :value="category.name"
                                    @input="update('name', $event)"
                                >
                                </v-text-field>
                            </v-flex>
                            <v-flex md4>
                                <v-btn color="primary" @click="save">Save</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { save_category } from '@/api/index.js'

    export default {
        name: 'admin-category-create',
        data () {
            return {
                category: {}
            }
        },
        methods: {
            update (param, value) {
                if (!value) {
                    value = false
                }
                this.$set(this.category, param, value)
            },
            save () {
                save_category(this.category).then(response => {
                    this.category = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully created category"
                    }
                    this.$router.push({name: 'admin_category'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            }
        },
    }
</script>
