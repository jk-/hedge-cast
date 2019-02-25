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
                            <v-flex md4>
                                <v-text-field
                                    label="Title"
                                    :value="item.title"
                                    @input="update('title', $event)"
                                >
                                </v-text-field>
                            </v-flex>
                            <v-flex md4>
                                <v-btn color="primary" @click="saveItem">Save</v-btn>
                            </v-flex>
                        </v-form>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import { get_video } from '@/api/index.js'

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
            saveItem () {
                save_video(this.item).then(response => {

                })
            }
        },
        created () {
            this.getItem()
        }
    }
</script>
