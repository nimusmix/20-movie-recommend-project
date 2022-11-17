<template>
  <div>
    <h1 class="h1">LandingView</h1>
    <div v-if="isLogin">
      <router-link :to="{ name: 'HomeView' }">들어가기</router-link>
    </div>
    <div v-else>
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> | 
      <router-link :to="{ name: 'SignupView' }">회원가입</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LandingView',
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getGenres() {
      this.$store.dispatch('getGenres')
    },
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
    this.getGenres()
  }
}
</script>

<style>

</style>