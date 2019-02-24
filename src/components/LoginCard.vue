<template>
    <v-layout>
        <v-flex xs12 sm6 offset-sm3>
            <v-card color="transparent z-depth-0">
                <v-toolbar color="z-depth-0">
                    <v-toolbar-title>Login</v-toolbar-title>
                </v-toolbar>
                <v-alert :value="errorMsg" error>{{ errorMsg }}</v-alert>
                <v-form
                    ref="form"
                    v-model="valid"
                    lazy-validation>
                    <v-container>
                        <v-layout>
                            <v-flex md12 lg12>
                                <v-text-field
                                v-model="username"
                                :rules="[rules.required]"
                                label="Username"
                                name="username"
                                autocomplete="username"
                                required
                                ></v-text-field>
                            </v-flex>
                        </v-layout>

                        <v-layout>
                            <v-flex md12 lg12>
                                <v-text-field
                                v-model="password"
                                :append-icon="pwShow ? 'visibility_off' : 'visibility'"
                                :rules="[rules.required]"
                                :type="pwShow ? 'text' : 'password'"
                                @click:append="pwShow = !pwShow"
                                label="passwword"
                                name="password"
                                autocomplete="current-password"
                                required
                                ></v-text-field>
                            </v-flex>
                        </v-layout>

                        <v-checkbox
                        v-model="checkbox"
                        label="Remember me"
                        ></v-checkbox>

                        <v-card-actions>
                            <v-btn color="primary" @click="authenticate">Login</v-btn>
                            <v-btn color="info" flat>forgot password?</v-btn>
                        </v-card-actions>
                    </v-container>
                </v-form>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>

import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import { EventBus } from '@/util/index.js'

export default {
    name: 'LoginCard',
    valid: false,
    mixins: [validationMixin],
    validations: {
      username: { required },
      password: { required }
    },
    data () {
        return {
            valid: true,
            checkbox: false,
            username: '',
            password: '',
            errorMsg: '',
            pwShow: false,
            rules: {
                required: value => !!value || 'Required.'
            }
        }
    },
    methods: {
        authenticate () {
            if (!this.$refs.form.validate()) {
                this.valid = false
            } else {
                this.valid = true
                this.errorMsg = ''
                this.$store.dispatch('login', { username: this.username, password: this.password })
            }
        },
    },
    mounted () {
        EventBus.$on('failedAuthentication', (msg) => {
            this.valid = false
            this.errorMsg = msg.response.data.message
        })
        EventBus.$on('successAuthentication', () => {
            this.$router.push('/')
        })
    },
    beforeDestroy () {
        EventBus.$off('failedAuthentication')
        EventBus.$off('successAuthentication')
    }
}
</script>
