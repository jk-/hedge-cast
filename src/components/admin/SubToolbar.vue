<template>
    <v-toolbar color="transparent z-depth-0">
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-flex md3>
            <v-text-field
                append-icon="search"
            ></v-text-field>
        </v-flex>
    </v-toolbar>
</template>


<script>
    export default {
        name: 'admin-sub-toolbar',
        props: ['title']
    }
</script>
