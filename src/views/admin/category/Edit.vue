<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing Category: {{ category.name }}</v-toolbar-title>
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
                                <v-btn color="primary" @click="saveCategory">Save</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_category } from '@/api/index.js'
    import { save_category } from '@/api/index.js'

    export default {
        name: 'admin-category-edit',
        data () {
            return {
                category: {}
            }
        },
        methods: {
            getCategory () {
                get_category(this.$route.params.id).then(response => {
                    this.category = response.data
                })
            },
            update (param, value) {
                if (!value) {
                    value = false
                }
                this.$set(this.category, param, value)
            },
            saveCategory () {
                save_category(this.category).then(response => {
                    this.category = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated category"
                    }
                    this.$router.push({name: 'admin_category'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            }
        },
        created () {
            this.getCategory()
        }
    }
</script>
