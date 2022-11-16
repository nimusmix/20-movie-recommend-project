<template>
  <div>
    <h1>LandingView</h1>
    <router-link :to="{ name: 'LoginView' }">로그인</router-link> | 
    <router-link :to="{ name: 'SignupView' }">회원가입</router-link>
  </div>
</template>

<script>
export default {
  name: 'LandingView',
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
  },
  created() {
    this.getMovies()
  }
}
</script>

<style>

</style>