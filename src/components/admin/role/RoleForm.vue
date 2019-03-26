<template>
    <v-form v-if="!isLoading"
        ref="form"
        :model="valid"
        lazy-validation>
        <v-flex md4>
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
            <v-btn v-if="editing" color="erorr" @click="remove">Remove</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import Role from '@/models/role'

    import { get_role } from '@/api/index.js'
    import { save_role } from '@/api/index.js'
    import { delete_role } from '@/api/index.js'

    export default {
        name: 'admin-role-edit',
        props: ['isEdit'],
        data () {
            return {
                item: Role,
                editing: this.isEdit,
                valid: true,
                isLoading: true,
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getItem () {
                get_role(this.$route.params.id).then(response => {
                    this.item = response.data
                    this.isLoading = false
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
                    save_role(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({ name: 'admin_role' })
                    })
                }
            },
            remove () {
                delete_role(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({ name: 'admin_role' })
                })
            }
        },
        created () {
            if (this.editing) {
                this.getItem()
            } else {
                this.isLoading = false
            }
        }
    }
</script>
