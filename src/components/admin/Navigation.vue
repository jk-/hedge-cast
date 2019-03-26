<template>
    <v-navigation-drawer
          absolute
          overflow
          app
          fixed
          permanent
          class="blue darken-4 white--text"
        >
        <v-toolbar flat>
          <v-list class="blue darken-4 white--text">
            <v-list-tile active-class="">
              <v-list-tile-title class="title">
                  Menu
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-toolbar>

        <v-divider></v-divider>

        <v-subheader>
            <v-subheader-title class="white--text">Admin</v-subheader-title>
        </v-subheader>

        <v-list class="pt-0 blue darken-4 white--text ">
            <v-list-tile
                v-for="item in items"
                :key="item.title"
                @click=""
                :to="{ name: item.path}"
                active-class="active"
            >

                <v-list-tile-avatar>
                    <v-icon class="white--text">{{ item.icon }}</v-icon>
                </v-list-tile-avatar>
                <v-list-tile-content>
                    <v-list-tile-title>
                        {{ item.title }}
                    </v-list-tile-title>
                </v-list-tile-content>
            </v-list-tile>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
    const admin_routes = [
        { title: "Users", path: 'admin_user', icon: 'person' },
        { title: "Category", path: 'admin_category', icon: 'folder' },
        { title: "Plans", path: 'admin_plan', icon: 'layers' },
        { title: "Playlists", path: 'admin_playlist', icon: 'playlist_play' },
        { title: "Roles", path: 'admin_role', icon: 'supervised_user_circle' },
        { title: "Videos", path: 'admin_video', icon: 'videocam' }
    ]

    export default {
        name: 'Navigation',
        data () {
            return {
                items: admin_routes
            }
        }
    }
</script>

<style lang="scss">

    @import "@/sass/materialize/components/_color-variables.scss";

    .active {
        color: color("blue", "darken-4");
        background-color: color("blue", "darken-2");
    }
    .v-list__tile--link:hover {
        background-color: color("blue", "darken-2") !important;
    }
</style>
