<template>
    <v-form
        ref="form"
        :model="valid"
        lazy-validation>
        <v-flex md9>
            <v-text-field
                label="Name"
                :value="item.name"
                :rules="[rules.required]"
                @input="update('name', $event)"
            >
            </v-text-field>
        </v-flex>
        <v-flex md4>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="error" @click="remove">Delete</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import Category from '@/models/category'

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
                item: Category,
                editing: this.isEdit,
                valid: true,
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getCategory () {
                get_category(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                if (value === null) {
                    value = 0
                }
                this.$set(this.item, param, value)
            },
            save () {
                if (!this.$refs.form.validate()) {
                    this.valid = false
                } else {
                    this.valid = true
                    save_category(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({name: 'admin_category'})
                    })
                }
            },
            remove () {
                delete_category(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({name: 'admin_category'})
                })
            }
        },
        created () {
            if (this.editing)
                this.getCategory()
        }
    }

</script>
