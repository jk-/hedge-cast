<template>
    <v-layout>
        <v-flex xs12 sm6 offset-sm3>
            <v-card color="transparent z-depth-0">
                <v-toolbar color="z-depth-0">
                    <v-toolbar-title>Login</v-toolbar-title>
                </v-toolbar>
                <v-form method="post" :action="url">
                    <v-container>
                        <v-layout>
                            <v-flex md12 lg12>
                                <v-text-field
                                label="Username"
                                name="username"
                                required
                                ></v-text-field>
                            </v-flex>
                        </v-layout>

                        <v-layout>
                            <v-flex md12 lg12>
                                <v-text-field
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
                            <v-btn type="submit" color="primary" @click="submit">Login</v-btn>
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

export default {
    name: 'LoginCard',
    props: ['url'],
    mixins: [validationMixin],
    validations: {
      uasername: { required },
      password: { required }
    },
    data () {
        return {
            valid: true,
            checkbox: false,
            pwShow: false,
            rules: {
                required: value => !!value || 'Required.'
            }
        }
    },
    methods: {
        submit () {
            this.$v.$touch()
        },
    }
}
</script>
