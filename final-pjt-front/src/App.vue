<template>
  <div id="app">
    <!-- navbar -->
    <nav class="navbar">
      <div class="profile">
        <img src="#" alt="logo" class="navbar-brand">
        <img src="#" alt="프로필 사진">
        <div class="dropdown">
          <button class="dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">username</button>
          <ul class="dropdown-menu">
            <li><a href="#" class="dropdown-item">내 프로필</a></li>
            <li><a href="#" class="dropdown-item">회원정보 수정</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a href="#" class="dropdown-item">로그아웃</a></li>
          </ul>
        </div>
      </div>
      <!-- <router-link :to="{ name: 'ArticleView' }">Articles</router-link> |  -->
    </nav>
    <router-view/>
  </div>
</template>

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