<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing User: {{ user.username }}</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
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
                                <v-btn color="error" @click="remove">Delete</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex md8>
                        <ul>
                            <li><strong>Created:</strong> {{ user.created | format_date }}</li>
                            <li><strong>Stripe ID:</strong> {{ user.stripe_customer_id | or_empty }}</li>
                            <li v-for="role in user.roles">
                                <strong>{{ role }}</strong>
                            </li>
                            <li><strong>Last Login:</strong> {{ user.last_login_at }}</li>
                            <li><strong>Referrer:</strong> {{ user.referrer | or_empty }}</li>
                        </ul>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_user } from '@/api/index.js'
    import { save_user } from '@/api/index.js'
    import { delete_user } from '@/api/index.js'

    export default {
        name: 'admin-edit-user',
        data () {
            return {
                user: {}
            }
        },
        methods: {
            getUser () {
                get_user(this.$route.params.id).then(response => {
                    this.user = response.data
                })
            },
            update (param, value) {
                if (!value) {
                    value = false
                }
                this.$set(this.user, param, value)
            },
            save () {
                save_user(this.user).then(response => {
                    this.user = response.data
                })
            },
            remove () {
                delete_user(this.user.id).then(response => {
                    this.user = {}
                    this.$router.push({name: "admin_user"})
                })
            }
        },
        created () {
            this.getUser()
        }
    }
</script>
