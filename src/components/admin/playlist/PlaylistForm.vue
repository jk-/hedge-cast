<template>
    <v-form v-if="!isLoading"
        ref="form"
        :model="valid">
        <v-flex md11>
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
        <VideoPlaylistCreator :is-edit="editing" :video-list="initialVideos" />
        <v-flex md11>
            <v-btn color="primary" @click="save">Save</v-btn>
            <v-btn v-if="editing" color="error" @click="remove">Delete</v-btn>
        </v-flex>
    </v-form>
</template>

<script>
    import Playlist from '@/models/playlist'
    import VideoPlaylistCreator from '@/components/admin/video/PlaylistCreator.vue'

    import { get_playlist } from '@/api/index.js'
    import { save_playlist } from '@/api/index.js'
    import { delete_playlist } from '@/api/index.js'
    import { get_all_categories } from '@/api/index.js'
    import { EventBus } from '@/util/index.js'

    export default {
        name: 'admin-playlist-form',
        props: ['isEdit'],
        data () {
            return {
                item: Playlist,
                editing: this.isEdit,
                categories: [],
                valid: true,
                isLoading: true,
                initialVideos: [],
                rules: {
                    required: value => !!value || 'Required.'
                }
            }
        },
        methods: {
            getItem () {
                console.log("getting item")
                get_playlist(this.$route.params.id).then(response => {
                    this.item = response.data
                    if (response.data.categories !== 'undefined')
                        this.item.categories = response.data.categories.map(x => x.name)

                    if (response.data.videos !== 'undefined')
                        this.initialVideos = response.data.videos

                    this.isLoading = false
                })
            },
            getCategories () {
                console.log("getting categories")
                get_all_categories().then(response => {
                    this.categories = response.data.map(x => x.name)
                })
            },
            update (param, value) {
                console.log("updating..")
                if (value === null) {
                    value = 0
                }
                this.$set(this.item, param, value)
            },
            save () {
                console.log("before validation", this.item)
                if (!this.$refs.form.validate()) {
                    this.valid = false
                } else {
                    console.log("after validation", this.item)
                    this.valid = true
                    save_playlist(this.item).then(response => {
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
            console.log("creating")
            if (this.editing) {
                this.getItem()
            } else {
                this.isLoading = false
            }
            this.getCategories()
        },
        mounted () {
            EventBus.$on('videoPlaylist', (videoList) => {
                this.item.videos = videoList
                console.log("received", this.item)
            })
        },
        beforeDestroy () {
            console.log("destroying event")
            EventBus.$off('videoPlaylist')
        },
        components: {
            VideoPlaylistCreator
        }
    }
</script>
