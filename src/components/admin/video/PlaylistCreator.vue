<template>
    <v-layout row>
        <v-flex md11>
            <v-autocomplete
                v-model="videoModel"
                :items="items"
                :loading="isLoading"
                :search-input.sync="search"
                item-value="id"
                item-text="title"
                color="white"
                hide-no-data
                hide-selected
                label="Videos"
                placeholder="Start typing to search"
                return-object
                dense
                box
            >
            </v-autocomplete>

            <table>
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">ID</th>
                        <th scope="col">Title</th>
                        <th scope="col">URL</th>
                        <th scope="col">Enabled</th>
                    </tr>
                </thead>
                <draggable v-model="videoList" tag="tbody">
                    <tr v-for="entry in videoList" :key="entry.id">
                        <td class="justify-center layout px-0">
                            <v-icon
                                small
                                @click="deleteItem(entry)"
                                >
                                delete
                            </v-icon>
                        </td>
                        <td>{{ entry.id }}</td>
                        <td>{{ entry.title }}</td>
                        <td>{{ entry.url }}</td>
                        <td>{{ entry.enabled | from_boolean }}</td>
                    </tr>
                </draggable>
            </table>
        </v-flex>
    </v-layout>
</template>

<script>

import { search_video } from '@/api/index.js'
import { EventBus } from '@/util/index.js'
import draggable from 'vuedraggable'

export default {
    name: 'admin-video-playlist-creator',
    props: ['isEdit', 'videoList'],
    data () {
        return {
            editing: this.isEdit,
            videoModel: null,
            videoList: [],
            isLoading: false,
            entries: [],
            search: null
        }
    },
    watch: {
        search (searchTerm) {
            if (!searchTerm) return
            if (this.isLoading) return

            this.isLoading = true

            search_video(searchTerm).then(response => {
                if (response.data.length)
                    this.entries = response.data
            }).finally(() => this.isLoading = false)
        },
        videoModel () {
            if (this.videoModel) {
                const pos = this.videoList.map(function(e) { return e.id; }).indexOf(this.videoModel.id);
                if (pos < 0) {
                    this.videoList.push(this.videoModel)
                } else {
                    this.$store.dispatch('setSnackbar', {
                        color: 'error',
                        text: 'That video is already in the playlist.'
                    })
                }
                this.videoModel = null
                this.entries = []
            }
        },
        videoList (newVideoList) {
            if (newVideoList !== "undefined") {
                console.log("EMITTING!")
                EventBus.$emit('videoPlaylist', newVideoList.map(x => x.id))
            }
        }
    },
    methods: {
        deleteItem (item) {
            const index = this.videoList.indexOf(item)
            this.videoList.splice(index, 1)
        },
    },
    components: {
        draggable
    },
    computed: {
        items () {
            return this.entries.map(entry => {
                const id = entry.id
                const title = entry.title
                return Object.assign({}, entry, { title, id })
            })
        }
    }
}
</script>
