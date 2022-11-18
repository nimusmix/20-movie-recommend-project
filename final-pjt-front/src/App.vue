<template>
  <div id="app" :class="mainclass">
    
    <div id="color-mode" >
      <nav id="col-nav">
        <a id="nav-logo" class="logo t-d-none">20.</a>
        <router-link :to="{ name: 'ProfileView', params: { username: username } }">{{ username }}</router-link>
        <div v-if="isLogin">
            <button @click="logout">로그아웃</button>                 <!-- 나중에 로그아웃 버튼 만들고 로그아웃 router link로 수정-->
          </div>
        <ul id="nav-ul">
          <li v-if="!isLogin">
            <router-link class="nav-item" :to="{ name: 'LoginView' }" >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M17 10H19C21 10 22 9 22 7V5C22 3 21 2 19 2H17C15 2 14 3 14 5V7C14 9 15 10 17 10ZM5 22H7C9 22 10 21 10 19V17C10 15 9 14 7 14H5C3 14 2 15 2 17V19C2 21 3 22 5 22ZM6 10C7.06087 10 8.07828 9.57857 8.82843 8.82843C9.57857 8.07828 10 7.06087 10 6C10 4.93913 9.57857 3.92172 8.82843 3.17157C8.07828 2.42143 7.06087 2 6 2C4.93913 2 3.92172 2.42143 3.17157 3.17157C2.42143 3.92172 2 4.93913 2 6C2 7.06087 2.42143 8.07828 3.17157 8.82843C3.92172 9.57857 4.93913 10 6 10V10ZM18 22C19.0609 22 20.0783 21.5786 20.8284 20.8284C21.5786 20.0783 22 19.0609 22 18C22 16.9391 21.5786 15.9217 20.8284 15.1716C20.0783 14.4214 19.0609 14 18 14C16.9391 14 15.9217 14.4214 15.1716 15.1716C14.4214 15.9217 14 16.9391 14 18C14 19.0609 14.4214 20.0783 15.1716 20.8284C15.9217 21.5786 16.9391 22 18 22Z" stroke-width="1.5" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              로그인
            </router-link>
          </li>
          <li v-if="!isLogin">
            <router-link  class="nav-item" :to="{ name: 'SignupView' }" >
              <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5.89 1.52L5.89 20.48M15.89 1.52L15.89 20.48M5.89 5.97L1.54 5.97M5.89 11L1.03 11M5.89 15.97L1.48 15.97M20.89 5.97L16.54 5.97M20.89 11L16.03 11M15.97 11L4.97 11M20.89 15.97L16.48 15.97M8 21L14 21C19 21 21 19 21 14L21 8C21 3 19 1 14 1L8 0.999999C3 0.999999 1 3 1 8L0.999999 14C0.999999 19 3 21 8 21Z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              회원가입
            </router-link>
          </li>
          <li 
          v-for="(routerName, routerLink, index) in routerLinks" :key="index"
          >
            <div class="li-inner-box">
              <router-link class="nav-item"  :to="{ name: routerLink }" >
                <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1.52 16.11H20.48M1.52 6.11H20.48M5.97 16.11V20.46M11 16.11V20.97M15.97 16.11V20.52M5.97 1.11V5.46M11 1.11V5.97M11 6.03V17.03M15.97 1.11V5.52M21 14V8C21 3 19 1 14 1H8C3 1 1 3 1 8V14C1 19 3 21 8 21H14C19 21 21 19 21 14Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <div class="v-a-middle">
                  {{ routerName }}
                </div>
              </router-link>
            </div>
          </li>
        </ul>
        <button @click="changeClass">변경하기</button>
      </nav>
      <router-view id="router-view" />
  </div>
  </div>
</template>
<script>
  export default {
    data(){
      return{
        mainclass:'light',
        routerLinks:{
          'LandingView': '랜딩페이지',
          'HomeView': '홈',
          'FeedView': '피드',
          'RecommendView': '추천영화',
          'CategoryView': '카테고리'
        }
      }
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      },
      username() {
        return this.$store.state.username
      }
    },
    methods: {
      logout() {
        this.$store.commit('LOGOUT')
      },
      changeClass(){
        if (this.mainclass != 'dark'){
          this.mainclass='dark'
        }else{
          this.mainclass='light'
        }
      }
    },
    updated() {
      this.$store.dispatch('getLoginUser')
      this.$store.dispatch('getGenres')
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getReviews')
    }
  }

</script>
<style lang="scss">
// 폰트세팅
  @import url('https://fonts.googleapis.com/css2?family=Manrope&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Unna&display=swap');
  @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

  $logo-font: 'Unna', serif;  // 순위2
  // $logo-font: 'Manrope', sans-serif;  //순위1
  $body-font: 'Pretendard Variable';

// 컬러세팅
  #app ,
  #app.light {
    //시맨틱 컬러
    --primary-color: #FF715E;
    --primary-color-15: #ff715e60;
    --primary-color-10: #ff715e23;
    --danger-color: #F16464 ;
    --warning-color: #F5AB35;
    --success-color: #47C1C3;
    --info-color: #00A0E1;
    --live-color:#42b983;

    //전역설정 컬러
    --bg-color:#FFF;
    --bg-router-color:#FFFAFA;
    --disable-color:#5F5F5F;
    --text-color:#000;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;
  }

  #app.dark {
    //시맨틱 컬러
    --primary-color: #FF715E;
    --primary-color-15: #ff715e24;
    --primary-color-10: #ff715e11;
    --danger-color: #F16464 ;
    --warning-color: #F5AB35;
    --success-color: #47C1C3;
    --info-color: #00A0E1;
    --live-color:#42b983;

    //전역설정 컬러
    --bg-color:#000;
    --bg-router-color:#1F1F1F;
    --disable-color:#c8c8c8;
    --text-color:#FFF;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;
  }
// 텍스트 스타일
  // 큰 텍스트 - h1
  $lg-font-size:2rem;
  $lg-font-weight:600;

  // 일반 텍스트 - 기본
  $main-font-size:1rem;
  $main-font-weight:400;

  // 본문 텍스트 - 얇게
  $main-font-weight-light:300;

  #app .h1 {
    font-size: $lg-font-size;
    font-weight: $lg-font-weight;
  }
  $trans-global:width 1s, height 1s, background-color 1s, transform 1s, border-color 1s, color 1s;
  $trans-global-fast:width 0.5s, height 0.5s, background-color 0.5s, transform 0.5s, border-color 0.5s, color 0.5s;
  $trans-global-very-fast:width 0.1s, height 0.1s, background-color 0.1s, transform 0.1s, border-color 0.1s, color 0.1s;
// button 스타일
  .button-list{
    .main-button{
      margin-right: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }
  .main-button {
    padding: 0.2rem 1rem;
    color:var(--primary-color);
    border: 1px solid var(--primary-color);
    background: none;
    border-radius: 30px;
    transition: $trans-global-fast;//$trans-global;
    &.selected{
      background-color: var(--primary-color);
      color:var(--button-live-text-color);
    }
    &:hover{
      background-color: var(--primary-color);
      color:var(--button-live-text-color);
    }
  }
// 전역 스타일
  #app {
    font-family:$body-font;
    background-color: var(--bg-router-color);
    color: var(--text-color);
    // -webkit-transition:width 2s, height 2s, background-color 2s, -webkit-transform 2s;
    transition: $trans-global;//$trans-global;
    font-size: $main-font-size;
    font-weight: $main-font-weight;
  }
  //텍스트 데코레이션
  .t-d-none{
    text-decoration: none;
  }
  // 로고
  .logo{
    font-family: $logo-font;
    font-weight: 600;
    font-size: 3rem;
  }

// 네비 스타일
  $nav-width:240px;
  #col-nav {
    min-width: $nav-width;
    position: fixed;
    height: 100%;
    overflow: auto;
    transition:$trans-global;
  }
  nav {
    $main-nav-padding-left:42px;
    background-color: var(--bg-color);
    svg {
      stroke: var(--disable-color);
    }
    
    #nav-ul{
      
      margin: 0px;
      padding: 0px;
      li{
        padding-left: $main-nav-padding-left;
        height: 56px;
        border-right: 5px solid var(--bg-color);
        svg{
          margin-right: 16px;
        }
        transition:$trans-global-fast;
      }
      li:hover{
       background-color: var(--primary-color-10);
       border-right: 5px solid var(--primary-color);
       transition:$trans-global-fast;
      }
      a {
        display: inline-block;
        vertical-align: middle;
        color: var(--disable-color);
        text-decoration: none;
        
      }
      li:hover a{
        color: var(--primary-color);
        svg {
          stroke: var(--primary-color);
        }
      }
      a.router-link-exact-active {
        color: var(--primary-color);
        svg {
          stroke: var(--primary-color);
        }
      }
    }
    #nav-logo {
      color: var(--text-color);
      display: block;
      text-align: center;
      padding: 0px $main-nav-padding-left;
      margin-top: 40px;
      margin-bottom: 40px;
    }
    .li-inner-box{
      width:100%;
      height:100%;
      position: relative;
    }
    .li-inner-box a{
      position: absolute;top: 50%;
      transform: translate(0%,-50%) /* 자식요소에 translate 값 주기*/
    }
    .v-a-middle{
      display: inline-block;
      vertical-align: middle;
    }
  }

  //라우터 뷰 전역설정
  #router-view{
    margin-left:$nav-width;
    padding-top: 48px;
    padding-left: 80px;
    min-height: 100vh;
  }
   
  
  // test











</style>
