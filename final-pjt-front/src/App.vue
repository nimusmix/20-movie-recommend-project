<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <div>
          <ul class="navbar-nav">
            <li class="nav-item"
            v-for="(routerName, routerLink, index) in routerLinks" :key="index"
            >
              <router-link :to="{ name: routerLink }" class="nav-link active">{{ routerName }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>
<script>
  export default {
    data(){
      return{
        routerLinks:{
          'LandingView':'랜딩페이지',
          'LoginView':'로그인',
          'SignupView':'회원가입',
          'HomeView':'홈',
          'FeedView':'피드',
          'RecommendView':'추천영화',
          'CategoryView':'카테고리'
        }
      }
    }
  }

</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>