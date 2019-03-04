<template>
    <div id="homepage">
        <v-img
            src="/dist/static/assets/img/hero.jpg"
            lazy-src="/dist/static/assets/img/hero-sm.jpg"
            gradient="to top right, rgba(0,0,0,.3), rgba(0,0,0,.35)">
            <Toolbar />
            <v-layout
                align-center
                justify-center
                column
                fill-height
                class="white--text"
            >
                <h1>Hero message</h1>
                <h4 class="subheading">Sub header</h4>
            </v-layout>
        </v-img>
        <v-container>
            <v-layout>
                <v-flex>

                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    import Toolbar from '@/components/Toolbar.vue'
    export default {
        name: 'home',
        components: {
            Toolbar
        }
    }
</script>

<style>
    .landing-bg {
    }
</style>
