<template>
    <v-form
        ref="form"
        :model="valid"
        lazy-validation>
        <v-flex md9>
            <v-text-field
                label="Username"
                :value="item.username"
                :rules="[rules.required]"
                @input="update('username', $event)"
                required
            >
            </v-text-field>
            <v-text-field
                label="Email"
                :value="item.email"
                :rules="[rules.required]"
                @input="update('email', $event)"
                required
            >
            </v-text-field>
            <v-text-field
                :append-icon="pwShow ? 'visibility_off' : 'visibility'"
                :type="pwShow ? 'text' : 'password'"
                :rules="[rules.required]"
                @click:append="pwShow = !pwShow"
                @input="update('password', $event)"
                label="Password"
                name="password"
                v-if="!editing"
                required
            ></v-text-field>
            <v-select
                v-model="item.roles"
                :items="roles"
                item-value="id"
                item-text="name"
                label="Roles"
                :menu-props="{closeOnContentClick:true}"
                attach
                chips
                multiple
            ></v-select>
            <v-checkbox
                :input-value="item.enabled"
                @change="update('enabled', $event)"
                label="Enabled"
            >
            </v-checkbox>
            <v-checkbox
                :input-value="item.can_email_notify"
                @change="update('can_email_notify', $event)"
                label="Allowed to email for notifications"
            >
            </v-checkbox>
            <v-checkbox
                :input-value="item.can_email_general"
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
                    <li><strong>Created:</strong> {{ item.created | format_date }}</li>
                    <li><strong>Last Login:</strong> {{ item.last_login_at }}</li>
                    <li><strong>Stripe ID:</strong> {{ item.stripe_customer_id }}</li>
                    <li>
                        <strong>Plans:</strong>
                        <span v-for="plan in item.plans">{{ plan.name }} </span>
                    </li>
                    <li><strong>Referrer:</strong> {{ item.referrer }}</li>
                </ul>
            </v-flex>
        </v-layout>
    </v-form>
</template>

<script>
    import User from '@/models/user'

    import { get_user } from '@/api/index.js'
    import { save_user } from '@/api/index.js'
    import { delete_user } from '@/api/index.js'
    import { get_all_roles } from '@/api/index.js'

    export default {
        name: 'admin-user-form',
        props: ['isEdit'],
        data () {
            return {
                item: User,
                roles: [],
                editing: this.isEdit,
                pwShow: false,
                valid: true,
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getUser () {
                get_user(this.$route.params.id).then(response => {
                    this.item = response.data
                    this.item.roles = response.data.roles.map(x => x.name)
                })
            },
            getRoles () {
                get_all_roles().then(response => {
                    this.roles = response.data.map(x => x.name)
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
                    save_user(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({ name: 'admin_user' })
                    })
                }
            },
            remove () {
                delete_user(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({ name: 'admin_user' })
                })
            }
        },
        created () {
            if (this.editing)
                this.getUser()
            this.getRoles()
        }
    }
</script>
