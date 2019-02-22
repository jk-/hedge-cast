<template>
    <div class="login">
        <Toolbar />
        <RegisterCard />
    </div>
</template>

<script>

    import RegisterCard from '../components/RegisterCard.vue'
    import Toolbar from '../components/Toolbar.vue'

    export default {
        name: 'Register',
        components: {
            RegisterCard,
            Toolbar
        }
    }
</script>
