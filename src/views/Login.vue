<template>
    <div class="login">
        <Toolbar />
        <LoginCard />
    </div>
</template>

<script>

    import LoginCard from '../components/LoginCard.vue'
    import Toolbar from '../components/Toolbar.vue'

    export default {
        name: 'Login',
        components: {
            LoginCard,
            Toolbar
        }
    }
</script>
