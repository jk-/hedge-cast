<template>
    <v-form>
        <v-flex md9>
            <v-text-field
                label="Name"
                :value="item.name"
                @input="update('name', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Code"
                :value="item.code"
                @input="update('code', $event)"
            >
            </v-text-field>

            <v-text-field
                label="Interval Term"
                :value="item.interval_term"
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
                @input="update('statement_desc', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Plan Group"
                :value="item.plan_group"
                @input="update('plan_group', $event)"
            >
            </v-text-field>

            <v-checkbox
                label="Enabled"
                :value="item.enabled"
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
                item: {},
                editing: this.isEdit
            }
        },
        methods: {
            getItem () {
                get_plan(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                this.$set(this.item, param, value)
            },
            save () {
                save_plan(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated plan"
                    }
                    this.$router.push({name: 'admin_plan'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            },
            remove () {
                delete_plan(this.item.id).then(response => {
                    this.item = response.data
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$router.push({name: 'admin_plan'})
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
