<template>
    <v-layout>
        <v-flex xs12 sm6 offset-sm3>
            <v-card color="transparent z-depth-0">
                <v-toolbar color="z-depth-0">
                    <v-toolbar-title>Login</v-toolbar-title>
                </v-toolbar>
                <p class="subtitle error-msg">{{ errorMsg }}</p>
                <v-container>
                    <v-layout>
                        <v-flex md12 lg12>
                            <v-text-field
                            v-model="username"
                            label="Username"
                            name="username"
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
                            label="passwword"
                            name="password"
                            required
                            @click:append="pwShow = !pwShow"
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
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>

import { validationMixin } from 'vuelidate'
import { required } from 'vuelidate/lib/validators'
import { EventBus } from '../util/index.js'

export default {
    name: 'LoginCard',
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
            this.$store.dispatch('login', { username: this.username, password: this.password })
        },
        register () {
            this.$store.dispatch('register', { username: this.username, password: this.password })
        }
    },
    mounted () {
        EventBus.$on('failedRegistering', (msg) => {
            this.errorMsg = msg
        })
        EventBus.$on('failedAuthentication', (msg) => {
            this.errorMsg = msg
        })
    },
    beforeDestroy () {
        EventBus.$off('failedRegistering')
        EventBus.$off('failedAuthentication')
    }
}
</script>
