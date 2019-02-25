<template>
    <v-snackbar v-model="snackbar.visible" :color="snackbar.color">
      {{ snackbar.text }}
      <v-btn
        dark
        flat
        @click="closeSnackbar"
      >
        Close
      </v-btn>
    </v-snackbar>
</template>

<script>
    import { mapMutations } from "vuex"

    export default {
        computed: {
            snackbar() {
              return this.$store.state.snackbar
            }
        },
        methods: {
            ...mapMutations(["closeSnackbar"])
        }
    }
</script>
