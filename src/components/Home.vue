<template>
    <div id="homepage">
        <v-img
            src="/dist/static/assets/img/hero.jpg"
            lazy-src="/dist/static/assets/img/hero-sm.jpg"
            gradient="to top right, rgba(0,0,0,.3), rgba(0,0,0,.35)"
        >
            <Toolbar />
            <v-layout
                align-center
                justify-center
                column
                fill-height
                class="white--text"
            >

            </v-layout>
        </v-img>
        <v-container>
            <v-layout row>
                <v-flex md4>
                    <v-card flat>
                        <v-card-title>
                            <span class="title font-weight-light">Category</span>
                        </v-card-title>
                        <v-card-text>
                            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex md4>
                    <v-card flat>
                        <v-card-title>
                            <span class="title font-weight-light">Category</span>
                        </v-card-title>

                        <v-card-text>
                            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex md4>
                    <v-card flat>
                        <v-card-title>
                            <span class="title font-weight-light">Category</span>
                        </v-card-title>

                        <v-card-text>
                            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
            <v-layout column align-center>
                <v-flex>
                    <v-btn round color="primary" dark>Browse Categories</v-btn>
                </v-flex>
            </v-layout>
        </v-container>
        <v-container>
            <v-layout column align-center>
                <v-flex md12>
                    <h4>Choose a Plan</h4>
                </v-flex>
            </v-layout>
            <v-layout row align-center justify-center>
                <v-flex md4>
                    <v-card flat>
                        <v-card-title>
                            <span class="title font-weight-light">Basic</span>
                        </v-card-title>

                        <v-card-text>
                            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                        </v-card-text>
                    </v-card>
                </v-flex>
                <v-flex md4>
                    <v-card flat>
                        <v-card-title>
                            <span class="title font-weight-light">Unlimited</span>
                        </v-card-title>

                        <v-card-text>
                            "Turns out semicolon-less style is easier and safer in TS because most gotcha edge cases are type invalid as well."
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-footer
            dark
            height="auto"
        >
            <v-card
            flat
            tile
            class="white--text text-xs-center"
            >
                <v-card-text>
                    <v-btn
                    v-for="icon in icons"
                    :key="icon"
                    class="mx-3 white--text"
                    icon
                    >
                        <v-icon size="24px">{{ icon }}</v-icon>
                    </v-btn>
                </v-card-text>

                <v-card-text class="white--text pt-0">
                    Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
                </v-card-text>

                <v-card-text class="white--text">
                    &copy;2018 — <strong>Hedge Cast</strong>
                </v-card-text>
            </v-card>
        </v-footer>
    </div>
</template>

<script>
    import Toolbar from '@/components/Toolbar.vue'
    export default {
        name: 'home',
        data () {
            return {
                icons: [
                    'twitter'
                ]
            }
        },
        components: {
            Toolbar
        }
    }
</script>
