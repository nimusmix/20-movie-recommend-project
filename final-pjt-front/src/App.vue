<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Navbar</a>
        <div>
          <ul class="navbar-nav">
            <div v-if="isLogin">
              <li class="nav-item">
                <button class="nav-link active" @click="logout">로그아웃</button>                 <!-- 나중에 로그아웃 버튼 만들고 로그아웃 router link로 수정-->
              </li>
            </div>
            <div v-else>
              <li class="nav-item">
                <router-links :to="{ name: LoginView }" class="nav-link active">로그인</router-links>
                <router-links :to="{ name: SignupView }" class="nav-link active">회원가입</router-links>
              </li>
            </div>
            <li class="nav-item"
            v-for="(routerName, routerLink, index) in routerLinks" :key="index"
            >
              <router-link :to="{ name: routerLink }" class="nav-link active">{{ routerName }}</router-link>
            </li>
            <!-- <li class="nav-item">
              <router-links :to="{ name: ProfileView }" class="nav-link active">{{ username }}</router-links>
            </li> -->
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
          'HomeView':'홈',
          'FeedView':'피드',
          'RecommendView':'추천영화',
          'CategoryView':'카테고리'
        }
      }
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      }
    },
    methods: {
      logout() {
        this.$store.commit('LOGOUT')
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