<template>
    <v-form v-if="!isLoading"
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
            <v-text-field
                label="Code"
                :value="item.code"
                :rules="[rules.required]"
                @input="update('code', $event)"
            >
            </v-text-field>

            <v-text-field
                label="Interval Term"
                :value="item.interval_term"
                :rules="[rules.required]"
                @input="update('interval_term', $event)"
            >
            </v-text-field>

            <v-text-field
                label="Interval Count"
                :value="item.interval_count"
                @input="update('interval_count', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Price"
                :value="item.price"
                @input="update('price', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Trial Days"
                :value="item.trial_days"
                @input="update('trial_days', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Statement Desc"
                :value="item.statement_desc"
                :rules="[rules.required]"
                @input="update('statement_desc', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Plan Group"
                :value="item.plan_group"
                :rules="[rules.required]"
                @input="update('plan_group', $event)"
            >
            </v-text-field>

            <v-checkbox
                label="Enabled"
                :input-value="item.enabled"
                @change="update('enabled', $event)"
            >
            </v-checkbox>
        </v-flex>
        <v-flex>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="erorr" @click="remove">Remove</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import Plan from '@/models/plan'
    import { get_plan } from '@/api/index.js'
    import { save_plan } from '@/api/index.js'
    import { delete_plan } from '@/api/index.js'

    export default {
        name: 'admin-plan-form',
        props: {
            isEdit: Boolean
        },
        data () {
            return {
                item: Plan,
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
                get_plan(this.$route.params.id).then(response => {
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
                    save_plan(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({ name: 'admin_plan' })
                    })
                }
            },
            remove () {
                delete_plan(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({ name: 'admin_plan' })
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
