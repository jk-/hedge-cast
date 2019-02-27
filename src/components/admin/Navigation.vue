<template>
    <v-navigation-drawer sm3 lg3 md3 permanent>
        <v-toolbar class="transparent z-depth-0">
          <v-list>
            <v-list-tile>
              <v-list-tile-title class="title">
                  Admin
              </v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-toolbar>

        <v-divider></v-divider>

        <v-list dense class="pt-0">
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            @click=""
            :to="{ name: item.path}"
          >
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
        { title: "Category", path: 'admin_category' },
        { title: "Plans", path: 'admin_plan' },
        { title: "Playlists", path: 'admin_playlist' },
        { title: "Roles", path: 'admin_role' },
        { title: "User", path: 'admin_user' },
        { title: "Videos", path: 'admin_video' },
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
