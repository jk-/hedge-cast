<template>
    <v-form>
        <v-flex md9>
            <v-text-field
                label="Name"
                :value="item.name"
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
    import { get_playlist } from '@/api/index.js'
    import { save_playlist } from '@/api/index.js'
    import { delete_playlist } from '@/api/index.js'

    export default {
        name: 'admin-playlist-form',
        props: ['isEdit'],
        data () {
            return {
                item: {},
                editing: this.isEdit
            }
        },
        methods: {
            getItem () {
                get_playlist(this.$route.params.id).then(response => {
                    this.item = response.data
                })
            },
            update (param, value) {
                this.$set(this.item, param, value)
            },
            save () {
                save_playlist(this.item).then(response => {
                    this.item = response.data
                    let payload = {
                        color: 'success',
                        text: "Sucessfully updated playlist"
                    }
                    this.$router.push({name: 'admin_playlist'})
                    this.$store.dispatch('setSnackbar', payload)
                })
            },
            remove () {
                delete_playlist(this.item.id).then(response => {
                    this.item = response.data
                    let payload = {
                        color: response.data.type,
                        text: response.data.message
                    }
                    this.$router.push({name: 'admin_playlist'})
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