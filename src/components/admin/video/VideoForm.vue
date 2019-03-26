<template>
    <v-form v-if="!isLoading"
        ref="form"
        :model="valid"
        lazy-validation>
        <v-flex md9>
            <v-text-field
                label="Title"
                :value="item.title"
                :rules="[rules.required]"
                @input="update('title', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Access Type"
                :value="item.access_type"
                :rules="[rules.required]"
                @input="update('access_type', $event)"
            >
            </v-text-field>
            <v-text-field
                label="URL"
                :value="item.url"
                @input="update('url', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Source"
                :value="item.source"
                @input="update('source', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Thumbnail"
                :value="item.thumbnail"
                @input="update('thumbnail', $event)"
            >
            </v-text-field>
            <v-checkbox
                label="Enabled"
                :value="item.enabled"
                @change="update('enabled', $event)"
            >
            </v-checkbox>
        </v-flex>
        <v-flex md4>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="erorr" @click="remove">Remove</v-btn>
        </v-flex>

        <v-layout row v-if="editing">
            <v-flex md8>
                <ul>
                    <li><strong>Created:</strong> {{ item.created | format_date }}</li>
                </ul>
            </v-flex>
        </v-layout>
    </v-form>
</template>

<script>
    import Video from '@/models/video'

    import { get_video } from '@/api/index.js'
    import { save_video } from '@/api/index.js'
    import { delete_video } from '@/api/index.js'

    export default {
        name: 'admin-video-form',
        props: ['isEdit'],
        data () {
            return {
                item: Video,
                editing: this.isEdit,
                valid: true,
                isLoading: true,
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getItem () {
                get_video(this.$route.params.id).then(response => {
                    this.item = response.data
                    this.isLoading = false
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
                    save_video(this.item).then(response => {
                        this.item = response.data
                        this.$router.push({ name: 'admin_video' })
                    })
                }
            },
            remove () {
                delete_video(this.item.id).then(response => {
                    this.item = {}
                    this.$router.push({ name: 'admin_video' })
                })
            }
        },
        created () {
            if (this.editing) {
                this.getItem()
            } else {
                this.isLoading = false
            }
        }
    }
</script>
