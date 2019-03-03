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
            <v-select
                v-model="item.categories"
                :items="categories"
                item-value="id"
                item-text="name"
                label="Categories"
                :menu-props="{closeOnContentClick:true}"
                attach
                chips
                multiple
            ></v-select>
            <v-checkbox
                label="Enabled"
                :input-value="item.enabled"
                @change="update('enabled', $event)"
            >
            </v-checkbox>
        </v-flex>
        <v-spacer></v-spacer>
        <v-flex md9>
            <v-text-field
                append-icon="search"
                label="Add video"
            ></v-text-field>
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
    import { get_all_categories } from '@/api/index.js'
    import { search_video } from '@/api/index.js'

    export default {
        name: 'admin-playlist-form',
        props: ['isEdit'],
        data () {
            return {
                item: Playlist,
                editing: this.isEdit,
                categories: [],
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
                    if (response.data.categories !== 'undefined')
                        this.item.categories = response.data.categories.map(x => x.name)
                })
            },
            getCategories () {
                get_all_categories().then(response => {
                    this.categories = response.data.map(x => x.name)
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
            this.getCategories()
        }
    }
</script>
