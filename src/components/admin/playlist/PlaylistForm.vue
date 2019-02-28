<template>
    <v-form
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
            <v-checkbox
                label="Enabled"
                :value="item.enabled"
                @change="update('enabled', $event)"
            >
            </v-checkbox>
            <span v-for="cat in item.category">{{ cat.name }}</span>
        </v-flex>
        <v-flex md4>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="error" @click="remove">Delete</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import Playlist from '@/models/playlist'
    import { get_playlist } from '@/api/index.js'
    import { save_playlist } from '@/api/index.js'
    import { delete_playlist } from '@/api/index.js'

    export default {
        name: 'admin-playlist-form',
        props: ['isEdit'],
        data () {
            return {
                item: Playlist,
                editing: this.isEdit,
                valid: true,
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getItem () {
                get_playlist(this.$route.params.id).then(response => {
                    this.item = response.data
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
                    save_playlist(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({ name: 'admin_playlist' })
                    })
                }
            },
            remove () {
                delete_playlist(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({ name: 'admin_playlist' })
                })
            }
        },
        created () {
            if (this.editing)
                this.getItem()
        }
    }
</script>
