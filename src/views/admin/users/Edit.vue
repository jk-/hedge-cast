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
                            <v-flex md4>
                                <v-text-field
                                    label="Username"
                                    :value="user.username"
                                    @input="update('username', $event)"
                                >
                                </v-text-field>
                            </v-flex>
                            <v-flex md4>
                                <v-text-field
                                    label="Email"
                                    :value="user.email"
                                    @input="update('email', $event)"
                                >
                                </v-text-field>
                            </v-flex>
                            <v-flex md4>
                                <v-checkbox
                                    :value="user.enabled"
                                    @change="update('enabled', $event)"
                                    label="Enabled"
                                >
                                </v-checkbox>
                            </v-flex>

                            <v-flex md4>
                                <v-checkbox
                                    :value="user.can_email_notify"
                                    @change="update('can_email_notify', $event)"
                                    label="Allowed to email for notifications"
                                >
                                </v-checkbox>
                            </v-flex>

                            <v-flex md4>
                                <v-checkbox
                                    :value="user.can_email_general"
                                    @change="update('can_email_general', $event)"
                                    label="Allowed to email for general purposes"
                                >
                                </v-checkbox>
                            </v-flex>
                            <v-flex md4>
                                <v-btn color="primary" @click="saveUser">Save</v-btn>
                            </v-flex>
                            <v-flex>
                                <v-subheader>Details</v-subheader>
                                <ul>
                                    <li><label>Created:</label> {{ user.created}}</li>
                                    <li><label>Stripe ID:</label> {{ user.stripe_customer_id }}</li>
                                    <li v-for="role in user.roles">
                                        <label>{{ role }}</label>
                                    </li>
                                </ul>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_user } from '@/api/index.js'
    import { save_user } from '@/api/index.js'

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
            saveUser () {
                save_user(this.user).then(response => {
                    this.user = response.data
                })
            }
        },
        created () {
            this.getUser()
        }
    }
</script>
