<template>
  <div class="router-view-padding">
    <h1 class="h1">LandingView</h1>
    
    <vue-typer
      :text='["Arya Stark","Jon Snow","Daenerys Targaryen","Melisandre","Tyrion Lannister"]'
      :repeat='Infinity'
      :shuffle='false'
      initial-action='typing'
      :pre-type-delay='70'
      :type-delay='91'
      :pre-erase-delay='2000'
      :erase-delay='250'
      erase-style='select-all'
      :erase-on-complete='false'
      caret-animation='smooth'
    ></vue-typer>

    
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
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
}
</script>

<style lang="scss">

label {
  display: inline-block;
  margin-bottom: 5px;
}

input {
  border-radius: 3px;
  padding: 1rem;
  font: inherit;
  border-color: black;
}
</style>