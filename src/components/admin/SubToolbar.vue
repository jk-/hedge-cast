<template>
    <v-toolbar color="white z-depth-0">
        <v-icon>{{ icon }}</v-icon>
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-flex md2>
            <v-text-field
                append-icon="search"
            ></v-text-field>
        </v-flex>
    </v-toolbar>
</template>


<script>
    export default {
        name: 'admin-sub-toolbar',
        props: ['icon', 'title']
    }
</script>
