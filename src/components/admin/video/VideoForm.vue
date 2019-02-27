<template>
    <v-form>
        <v-flex md9>
            <v-text-field
                label="Title"
                :value="item.title"
                @input="update('title', $event)"
            >
            </v-text-field>
            <v-text-field
                label="Access Type"
                :value="item.access_type"
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
                @input="update('enabled', $event)"
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
    import { get_video } from '@/api/index.js'
    import { save_video } from '@/api/index.js'
    import { delete_video } from '@/api/index.js'

    export default {
        name: 'admin-video-form',
        props: ['isEdit'],
        data () {
            return {
                item: {},
                editing: this.isEdit
            }
        },
        methods: {
            getItem () {
                get_video(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                this.$set(this.item, param, value)
            },
            save () {
                save_video(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated video"
                    }
                    this.$router.push({name: 'admin_video'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            },
            remove () {
                delete_video(this.item.id).then(response => {
                    this.item = response.data
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$router.push({name: 'admin_video'})
                    this.$store.dispatch('setSnackbar', payload)

                })
            }
        },
        created () {
            if (this.editing)
                this.getItem()
        }
    }
</script>
