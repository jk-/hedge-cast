<template>
    <v-form>
        <v-flex md9>
            <v-text-field
                label="Username"
                :value="user.username"
                @input="update('username', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Email"
                :value="user.email"
                @input="update('email', $event)"
            >
            </v-text-field>
            <v-checkbox
                :value="user.enabled"
                @change="update('enabled', $event)"
                label="Enabled"
            >
            </v-checkbox>
            <v-checkbox
                :value="user.can_email_notify"
                @change="update('can_email_notify', $event)"
                label="Allowed to email for notifications"
            >
            </v-checkbox>
            <v-checkbox
                :value="user.can_email_general"
                @change="update('can_email_general', $event)"
                label="Allowed to email for general purposes"
            >
            </v-checkbox>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="error" @click="remove">Delete</v-btn>
        </v-flex>

        <v-layout row v-if="editing">
            <v-flex md8>
                <ul>
                    <li><strong>Created:</strong> {{ user.created | format_date }}</li>
                    <li><strong>Stripe ID:</strong> {{ user.stripe_customer_id | or_empty }}</li>
                    <li>
                        <strong>Roles:</strong>
                        <span v-for="role in user.roles">{{ role.name }} </span>
                    </li>
                    <li>
                        <strong>Plans:</strong>
                        <span v-for="plan in user.plans">{{ plan.name }} </span>
                    </li>
                    <li><strong>Last Login:</strong> {{ user.last_login_at }}</li>
                    <li><strong>Referrer:</strong> {{ user.referrer | or_empty }}</li>
                </ul>
            </v-flex>
        </v-layout>
    </v-form>
</template>

<script>
    import { get_user } from '@/api/index.js'
    import { save_user } from '@/api/index.js'
    import { delete_user } from '@/api/index.js'

    export default {
        name: 'admin-user-form',
        props: ['isEdit'],
        data () {
            return {
                user: {},
                editing: this.isEdit
            }
        },
        methods: {
            getUser () {
                get_user(this.$route.params.id).then(response => {
                    this.user = response.data
                    console.log(this.user.plan)
                })
            },
            update (param, value) {
                this.$set(this.user, param, value)
            },
            save () {
                save_user(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated user"
                    }
                    this.$router.push({name: 'admin_user'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            },
            remove () {
                delete_user(this.item.id).then(response => {
                    this.item = response.data
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$router.push({name: 'admin_user'})
                    this.$store.dispatch('setSnackbar', payload)

                })
            }
        },
        created () {
            if (this.editing)
                this.getUser()
        }
    }
</script>
