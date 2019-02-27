<template>
    <v-layout white>
        <v-flex>
            <v-layout row>
                <v-toolbar color="transparent z-depth-0">
                    <v-toolbar-title>Editing Video: {{ item.title }}</v-toolbar-title>
                </v-toolbar>
            </v-layout>
            <v-container>
                <v-layout row>
                    <v-flex md12>
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
                                <v-btn color="primary" @click="saveItem">Save</v-btn>
                                <v-btn color="erorr" @click="remove">Remove</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex md8>
                        <ul>
                            <li><strong>Created:</strong> {{ item.created | format_date }}</li>
                        </ul>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_video } from '@/api/index.js'
    import { save_video } from '@/api/index.js'

    export default {
        name: 'admin-video-edit',
        data () {
            return {
                item: {}
            }
        },
        methods: {
            getItem () {
                get_video(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                if (!value) {
                    value = false
                }
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
                remove_video(this.item.id).then(response => {
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
            this.getItem()
        }
    }
</script>
