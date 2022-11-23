<template>
  <div id="app" :class="mainclass">

      <nav id="col-nav" v-if="isLogin">
        <div id="nav-logo" class="logo t-d-none cusor-pointer" @click="goToHome">20.</div>

        <div id="nav-profile-box">
          <div id="nav-profile-img-box" class="cusor-pointer inner-shadow">
            <img class="img-circle-80" v-if="loginUser?.profile_img" :src="`http://127.0.0.1:8000${loginUser?.profile_img}`" @click="goToProfile">
            <img class="img-circle-80" v-else src="@/assets/basic.png" @click="goToProfile">
          </div>
          <div style="height: 0.4rem;"></div>
          <div v-if="isLogin" style="margin-bottom:30px">
            <b-dropdown id="dropdown-1" :text="loginUser?.username"  variant="namecolor"  class="m-md-2">
              <b-dropdown-item @click="goToProfile">내 프로필</b-dropdown-item>
              <b-dropdown-item @click="logout">로그아웃</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item @click="changeClass" v-if="this.mainclass === 'light'">다크모드</b-dropdown-item>
              <b-dropdown-item @click="changeClass" v-else>라이트모드</b-dropdown-item>
            </b-dropdown>
          </div>
        </div>

        <ul id="nav-ul">
          <div v-if="!isLogin">
            <li
              v-for="loginNav, index in loginList" :key="index"
            >
              <div class="li-inner-box cusor-pointer" @click="goToLink(loginNav.routerLink)">
                <router-link class="nav-item" :to="{ name: loginNav.routerLink }" >
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12.1198 12.78C12.0401 12.77 11.9595 12.77 11.8798 12.78C11.0317 12.7514 10.228 12.3944 9.63831 11.7842C9.04866 11.174 8.71929 10.3585 8.71977 9.50999C8.71977 7.69999 10.1798 6.22999 11.9998 6.22999C12.8592 6.22849 13.6848 6.5648 14.2986 7.16639C14.9124 7.76798 15.2652 8.58668 15.2809 9.44597C15.2966 10.3053 14.9741 11.1363 14.3827 11.76C13.7914 12.3837 12.9787 12.75 12.1198 12.78V12.78ZM18.7398 19.38C16.902 21.0691 14.4958 22.0044 11.9998 22C9.39977 22 7.03977 21.01 5.25977 19.38C5.35977 18.44 5.95977 17.52 7.02977 16.8C9.76977 14.98 14.2498 14.98 16.9698 16.8C18.0398 17.52 18.6398 18.44 18.7398 19.38V19.38Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <div class="v-a-middle">
                    {{ loginNav.routerName }}
                  </div>
                </router-link>
              </div>
            </li>
          </div>
        <div v-else>
          <li 
          v-for="routerNav, index in routerList" :key="index"
          >
            <div class="li-inner-box cusor-pointer" @click="goToLink(routerNav.routerLink)">
              <router-link class="nav-item"  :to="{ name: routerNav.routerLink }" >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" >
                    <path :d="routerNav.path"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <div class="v-a-middle">
                  {{ routerNav.routerName }}
                </div>
              </router-link>
            </div>
          </li>
        </div>
      </ul>
    </nav>
    <!-- <router-view id="router-view"/> -->
    <router-view :id="isLogin ? 'router-view' : 'router-view-user'"/>
  </div>
</template>

<script>
  export default {
    data() {
      return{
        mainclass:'light',
        loginList: [
          {
            'routerLink':'LoginView',
            'routerName':'로그인',
            'path': 'M12.1198 12.78C12.0401 12.77 11.9595 12.77 11.8798 12.78C11.0317 12.7514 10.228 12.3944 9.63831 11.7842C9.04866 11.174 8.71929 10.3585 8.71977 9.50999C8.71977 7.69999 10.1798 6.22999 11.9998 6.22999C12.8592 6.22849 13.6848 6.5648 14.2986 7.16639C14.9124 7.76798 15.2652 8.58668 15.2809 9.44597C15.2966 10.3053 14.9741 11.1363 14.3827 11.76C13.7914 12.3837 12.9787 12.75 12.1198 12.78V12.78ZM18.7398 19.38C16.902 21.0691 14.4958 22.0044 11.9998 22C9.39977 22 7.03977 21.01 5.25977 19.38C5.35977 18.44 5.95977 17.52 7.02977 16.8C9.76977 14.98 14.2498 14.98 16.9698 16.8C18.0398 17.52 18.6398 18.44 18.7398 19.38V19.38Z',
          },
          // {
          //   'routerLink':'SignupView',
          //   'routerName':'회원가입',
          //   'path': '',
          // }
        ]
        ,
        routerList: [
          // {
          //   'routerLink':'LandingView',
          //   'routerName':'랜딩페이지',
          //   'path': '',
          // },
          {
            'routerLink':'HomeView',
            'routerName':'홈',
            'path': 'M11.9998 17.9998V14.9998M10.0698 2.81985L3.13978 8.36985C2.35978 8.98985 1.85978 10.2998 2.02978 11.2798L3.35978 19.2398C3.59978 20.6598 4.95978 21.8098 6.39978 21.8098H17.5998C19.0298 21.8098 20.3998 20.6498 20.6398 19.2398L21.9698 11.2798C22.1298 10.2998 21.6298 8.98985 20.8598 8.36985L13.9298 2.82985C12.8598 1.96985 11.1298 1.96985 10.0698 2.81985V2.81985Z',
          },
          {
            'routerLink':'FeedView',
            'routerName':'피드',
            'path': 'M5.5 4V2.25M9.5 4V2.25M13.5 4V2.25M2 12H17.51M17.79 10.47V17.79C17.79 18.9066 17.3464 19.9774 16.5569 20.7669C15.7674 21.5564 14.6966 22 13.58 22H6.21C3.89 22 2 20.11 2 17.79V10.47C2 9.35344 2.44355 8.28261 3.23308 7.49308C4.02261 6.70355 5.09344 6.26 6.21 6.26H13.58C15.9 6.26 17.79 8.15 17.79 10.47V10.47ZM22 13.16C22 15.48 20.11 17.37 17.79 17.37V8.95C18.3429 8.95 18.8903 9.05889 19.4011 9.27047C19.9119 9.48204 20.376 9.79215 20.7669 10.1831C21.1579 10.574 21.468 11.0381 21.6795 11.5489C21.8911 12.0597 22 12.6071 22 13.16V13.16Z',
          },
          {
            'routerLink':'RecommendView',
            'routerName':'추천영화',
            'path': 'M2.52 17.11H21.48M2.52 7.11H21.48M6.97 17.11V21.46M12 17.11V21.97M16.97 17.11V21.52M6.97 2.11V6.46M12 2.11V6.97M12 7.03V18.03M16.97 2.11V6.52M22 15V9C22 4 20 2 15 2H9C4 2 2 4 2 9V15C2 20 4 22 9 22H15C20 22 22 20 22 15Z',
          },
          {
            'routerLink':'CategoryView',
            'routerName':'카테고리',
            'path': 'M17 10H19C21 10 22 9 22 7V5C22 3 21 2 19 2H17C15 2 14 3 14 5V7C14 9 15 10 17 10ZM5 22H7C9 22 10 21 10 19V17C10 15 9 14 7 14H5C3 14 2 15 2 17V19C2 21 3 22 5 22ZM6 10C7.06087 10 8.07828 9.57857 8.82843 8.82843C9.57857 8.07828 10 7.06087 10 6C10 4.93913 9.57857 3.92172 8.82843 3.17157C8.07828 2.42143 7.06087 2 6 2C4.93913 2 3.92172 2.42143 3.17157 3.17157C2.42143 3.92172 2 4.93913 2 6C2 7.06087 2.42143 8.07828 3.17157 8.82843C3.92172 9.57857 4.93913 10 6 10V10ZM18 22C19.0609 22 20.0783 21.5786 20.8284 20.8284C21.5786 20.0783 22 19.0609 22 18C22 16.9391 21.5786 15.9217 20.8284 15.1716C20.0783 14.4214 19.0609 14 18 14C16.9391 14 15.9217 14.4214 15.1716 15.1716C14.4214 15.9217 14 16.9391 14 18C14 19.0609 14.4214 20.0783 15.1716 20.8284C15.9217 21.5786 16.9391 22 18 22Z',
          },
        ]
      }
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      },
      loginUser() {
        return this.$store.state.loginUser
      },
      width(){
        return this.$store.state.width
      },
      height(){
        return this.$store.state.height
      }
    },
    methods: {
      logout() {
        this.$store.commit('LOGOUT')
      },
      changeClass() {
        if (this.mainclass != 'dark') {
          this.mainclass='dark'
        } else {
          this.mainclass='light'
        }
      },
      
      goToLink(routerLink) {
        this.$router.push({ name: routerLink })
          .catch(() => {})
      },
      goToHome() {
        this.$router.push({ name: 'HomeView' })
          .catch(() => {})
      },
      goToProfile() {
        this.$router.push({ name: 'ProfileView', params: { username: this.loginUser.username } })
        .catch(() => {})
      },
      handleResize(){
        this.$store.dispatch('getWindowSize')
        // console.log('test')
      }
    },
    created() {
      this.$store.dispatch('getGenres')
      this.$store.dispatch('getMovies')
      this.$store.dispatch('getReviews')
    },
    updated() {
      // this.$store.dispatch('getGenres')
      // this.$store.dispatch('getMovies')
      // this.$store.dispatch('getReviews')
      this.$store.dispatch('getWindowSize')
      window.addEventListener('resize', this.handleResize);
      // console.log(window.innerHeight)
      // console.log(window.innerWidth)
    },
    mounted(){ 
    },
  }

</script>
<style lang="scss">
// 폰트세팅
  @import url('https://fonts.googleapis.com/css2?family=Manrope&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Unna&display=swap');
  @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

  // $logo-font: 'Unna', serif;  // 순위2
  $logo-font: 'Manrope', sans-serif;  //순위1
  $body-font: 'Pretendard Variable';

// 컬러세팅
  #app ,
  #app.light {
    //시맨틱 컬러
    --primary-color: #FF715E;
    --primary-color-50: #ff715e83;
    --primary-color-15: #ff715e60;
    --primary-color-10: #ff715e23;
    --danger-color: #F16464 ;
    --warning-color: #F5AB35;
    --success-color: #47C1C3;
    --info-color: #00A0E1;
    --live-color:#42b983;

    //전역설정 컬러
    --bg-color:#FFF;
    --bg-router-color:#fbf6f7;
    --disable-color:#5F5F5F;
    --text-color:#000;
    --text-color-80:rgba(0, 0, 0, 0.8);
    --text-color-30:rgba(0, 0, 0, 0.3);
    --text-color-0:#0000;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;

    //피드 및 네비 그림자
    --feed-shadow:rgba(0, 0, 0, 0.03);
    --feed-hover-shadow:rgba(0, 0, 0, 0.202);

    //프로필 이미지 외곽선
    --img-border:rgba(0, 0, 0, 0.05);
    --inner-shadow:rgba(0, 0, 0, 0.05);
  }

  #app.dark {
    //시맨틱 컬러
    --primary-color: #FF715E;
    --primary-color-50: #ff715e83;
    --primary-color-15: #ff715e6b;
    --primary-color-10: #ff715e4f;
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
    --text-color-80:rgba(255, 255, 255, 0.8);
    --text-color-30:rgba(225, 225, 225, 0.19);
    --text-color-0:#FFF0;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;
    
    //피드 그림자
    --feed-shadow:rgb(255, 255, 255, 0.01);
    --feed-hover-shadow:rgba(255, 255, 255, 0.3);

    //프로필 이미지 외곽선
    --img-border:rgb(255, 255, 255, 0.3);
    --inner-shadow:rgb(255, 255, 255, 0.1); 
  }
// 텍스트 스타일
  // 큰 텍스트 - h1
  $lg-font-size:2rem;
  $lg-font-weight:600;

  // 일반 텍스트 - 기본
  $main-font-size:1.0rem;
  $main-font-weight:300;

  // 영화카드
  $movie-h3-font: 1.2rem;
  // 본문 텍스트 - 얇게
  $main-font-weight-light:300;

// 애니메이션 스타일
  $trans-global:width 1s, height 1s, background-color 1s, transform 1s, border-color 1s, color 1s, box-shadow 1s;
  $trans-global-fast:width 0.5s, height 0.5s, background-color 0.5s, transform 0.5s, border-color 0.5s, color 0.5s, box-shadow 0.5s;
  $trans-global-very-fast:width 0.1s, height 0.1s, background-color 0.1s, transform 0.1s, border-color 0.1s, color 0.1s, box-shadow 0.1s;

// border 스타일
  $border-radius-4: 4px;
  $border-radius-8: 6px;
  $border-radius-12: 12px;

  // 
  .circle{
    border-radius: 50%;
  }

  .img-circle-80 {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 1px solid var(--img-border);
  }
  
  .img-circle-100 {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 1px solid var(--img-border);
    
  }

  .img-circle-ott {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 1px solid var(--img-border);
  }

  .cicle-lr{
    border-radius: 32px;
  }
  .inner-shadow{
    box-shadow: inset 4px 4px 15px var(--inner-shadow);
  }

  // 전역설정
  #app .h1 {
    font-size: $lg-font-size;
    font-weight: $lg-font-weight;
    margin-bottom: 24px;
  }
  #app .h2 {
    font-size: 1.6rem;
    font-weight: $lg-font-weight;
    margin-bottom: 0.8rem;
    span{
      font-weight: 400;
    }
  }

  #app .h3 {
    font-size: $movie-h3-font;
    font-weight: $lg-font-weight;
    margin-bottom: 0.8rem;
  }

  #app .h3 a{
    font-size: $movie-h3-font;
    font-weight: $lg-font-weight;
  }

// 여백 스타일
.space {
    height: 56px;
  }
// 그림자 스타일
$shadow-default: 4px 0px 20px var(--feed-shadow);
$shadow-hover: 4px 0px 20px var(--feed-hover-shadow);
$shadow-primary: 0px 0px 10px 0px var(--primary-color-15);
$shadow-focus: 0px 0px 10px 2px var(--primary-color-50);

// button 스타일
  .button-list {
    .main-button {
      margin-right: 0.5rem;
      margin-bottom: 0.5rem;
    }
  }

  .main-button {
    padding: 0.2rem 1rem;
    color: var(--primary-color);
    border: 1px solid var(--primary-color);
    background: none;
    border-radius: 30px;
    transition: $trans-global-very-fast;//$trans-global;
    
    &.selected {
      background-color: var(--primary-color);
      color:var(--button-live-text-color);
    }
    &:hover {
      box-shadow: $shadow-focus;
      transition: $trans-global-fast;
      // background-color: var(--primary-color-15);
      // color:var(--button-live-text-color);
    }
    &:active{
      background: none;
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

  // 커서 스타일
  .cusor-pointer{
    cursor: pointer;
  }

  // 로고
  .logo {
    font-family: $logo-font;
    // font-weight: 600;
    font-weight: 300;
    font-size: 3rem;
  }

// 네비 스타일
  $nav-width: 240px;
  #col-nav {
    min-width: $nav-width;
    position: fixed;
    height: 100%;
    overflow: auto;
    transition:$trans-global;
    box-shadow: $shadow-default;
  }
  #dropdown-1{
    #dropdown-1__BV_toggle_{
      color: var(--text-color-80);
    }
    li:active{
        background-color: #F16464;
    }
    a:active{
        background-color: #F16464;
    }
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
      li {
        height: 56px;
        border-right: 5px solid var(--bg-color);
        transition:$trans-global-fast;

        svg {
          margin-right: 16px;
        }
      }

      li:hover {
        background-color: var(--primary-color-10);
        border-right: 5px solid var(--primary-color);
        transition:$trans-global-fast;
      }

      a {
        padding-left: $main-nav-padding-left;
        display: inline-block;
        vertical-align: middle;
        color: var(--disable-color);
        text-decoration: none;
      }

      li:hover a {
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
      margin-top: 100px;
      margin-bottom: 60px;
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
    margin-left: $nav-width;
    min-height: 100vh;
  }

  #router-view-user{
    min-height: 100vh;
  }

  @function w_to_h() {
        
  }

  .router-view-padding {
      padding: 56px 56px 56px 56px;
    }


  // 홈
  //가로스크롤 리스트
  .row-scroll {
    overflow: auto;
    white-space: nowrap;
    .row-scroll-item {
      display: inline-block;
      width: 200px;
      margin-right: 20px;
    }
  }
  //가로스크롤
  .row-scroll::-webkit-scrollbar {
    width: 0px;  /* 스크롤바의 너비 */
    height: 0px;
  }
  .row-scroll::-webkit-scrollbar-thumb {
      height: 5%; /* 스크롤바의 길이 */
      width: 5%; /* 스크롤바의 길이 */
      background: var(--primary-color-15); /* 스크롤바의 색상 */
      border-radius: 10px;
  }

  .row-scroll::-webkit-scrollbar-track {
      background: none;  /*스크롤바 뒷 배경 색상*/
      border-radius: 10px;
  }

  .row-scroll-button{
    position:absolute;
    border: none;
    height: 80px;
    width: 80px;
    padding: 20px;
    font-weight: 900;
    top:50%;
    transform: translate(0%,-50%);
    border-radius: 50%;
    color: var(--bg-color);
    background-color: var(--text-color-30);
    transition: left 0.1s, right 0.1s, width 0.5s, height 0.4s, border-radius 0.5s, background-color 0.5s, transform 0.5s, border-color 0.5s, color 0.5s, box-shadow 0.5s;
    box-shadow: $shadow-default;
    z-index: 11;
    &.r-s-b-left{
      left: -16px; 
      &:hover{
        background: linear-gradient(90deg, var(--text-color), var(--text-color-0));
        left: 0px;
        height: 100%;
        width: 200px;
        border-radius: 0%;
        border-top-right-radius: 50%;
        border-bottom-right-radius: 50%;
      }
    }
    
    &.r-s-b-right{
      right: -16px;
      &:hover{
        background: linear-gradient(270deg, var(--text-color), var(--text-color-0));
        height: 100%;
        width: 200px;
        right: 0px;
        border-radius: 0%;
        border-top-left-radius: 50%;
        border-bottom-left-radius: 50%;
      }
    }
  }


  // 영화카드
  .movie-card {
    display: block;
    border-radius: 8px;
    transition: $trans-global-fast;
    padding:8px;
    cursor: pointer;
    .logos {
      position: absolute;
      z-index: 3;
      margin: 5px;
      // margin-left: auto;
      // margin-right: auto;
      img {
        margin: 1.2px;
        box-shadow:$shadow-hover;
        
      }
    }
    &:hover{
      box-shadow:$shadow-hover;
      background-color: var(--bg-color);
    }
    a {
      color: var(--text-color);
      
      .card-img-top {
        width: 100%;
        aspect-ratio: 3.5 / 5;
        object-fit: cover;
        border-radius: $border-radius-8;
      }

      h3 {
        margin: 0.4rem 0px 0px 0px;
      }

      a {
        font-size: $main-font-size;
      }

      .movie-card-title {
        margin-top: 0.8rem;
        margin-bottom: 0.4rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }

      .movie-card-detail {
        margin: 0px;
      }
    }
  }

  // 피드 아이템
  .feed-item {
    display: flex;
    border: none;
    width: 500px;
    height: 148px;
    background: var(--bg-color);
    box-shadow: $shadow-default;
    border-radius: $border-radius-8;
    padding: 0rem 0rem;
    margin-bottom: 0.8rem;

    img {
      display: inline-block;
      height: inherit;
      aspect-ratio: 3.5 / 5;
      border-top-left-radius: $border-radius-8;
      border-bottom-left-radius: $border-radius-8;
      // object-fit: cover;
      // overflow: hidden;
    }
    .feed-nospo{
      color: var(--text-color-80)
    }
    .feed-item-contents {
      display: inline-block;
      width: 392px;
      padding: 1rem 1rem;
    }

    .feed-item-name {
      display:inline-block;
    }

    .feed-item-lasttime {
      display:inline-block;
      color: var(--disable-color);
    }
  }
  

  // 리뷰 만들 때
  #REVIEW_CREATE {
    border: 1px solid var(--primary-color-10);
    padding: 1rem 1.5rem ;
    background: var(--bg-color);
    border-radius: 8px;
    // border-color: ;
    box-shadow: $shadow-primary;

    transition: 0.1s;
    &:hover{
      border: 1px solid var(--primary-color-50);
      box-shadow: $shadow-focus;
    }
    &:focus-within{
      border: 1px solid var(--primary-color-50);
      box-shadow: $shadow-focus;
    }
    
    .logo {
      display: inline-block;
    }

    input {
      color: var(--disable-color);
      background-color: none;
      border: none;
    }
  }
  // 별
  output.b-rating {
    margin: 0px;
    padding: 0px;
    height: 0px;
    border: none;
  }
      
  .star-rating {
    background-color: none;

    .b-rating-star {
      margin: 0px;
      padding: 4px;
    }

    .b-rating-icon {
      color: var(--primary-color);
      margin: 0px;
      padding: 0px;

      svg {
        min-width:1px;
      }
    }
  }

  .user-input {
    margin: 10px 0px;
    text-align: center;
    background: transparent;
    border: none;
    border-bottom: 1px solid black;
    outline: none;
  }

  .err-msg {
    color: var(--danger-color);
  }

  .profile-img-box {
    width: 140px;
    height: 140px;
    border-radius: 70%;
    overflow: hidden;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  #nav-profile-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    #nav-profile-img-box {
      width: 80px;
      height: 80px;
      border-radius: 70%;
      overflow: hidden;

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }
  }
  // 프로필
  .head-box {
    display: flex;
    align-items: center;

    .detail-box{
      display: flex;
      flex-direction: column;
      margin-left: 2rem;

      .user-and-button {
        display: flex;
        justify-content: space-between;
        align-items: center;

        .space {
          width: 5.2rem;
        }
      }

      .follow-info {
        display: flex;
      }
    }
  }

  //모달
  .collection-modal {
    position: absolute;
  }
  
  #MODAL{
    border-radius: 8px;
  }
  .overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 10;
    background-color: black;
  }

  .modal-card{
   -ms-overflow-style: none;
  }


  .modal-card {
    position: fixed;
    width: 70%;
    top: 50%;
    left: 15%;
    transform: translate(0%,-50%);
    margin-left: auto;
    margin-right: auto;
    z-index: 11;
    padding: 40px;
    background-color: white;
  }

  .modal-movie{
    width: 200px;
  }

  .center-head{
    display: flex;
    justify-content: center;
    margin: 2rem 0px;
  }



.vue-typer {
  .custom.char {
    font-family: $body-font;
  }
  .custom.char.typed {
    color: var(--text-color);
  }
  .custom.char.selected {
    color: var(--primary-color);
  }
}

.custom.caret {
  animation: rocking 0.1s ease-in-out 0s infinite;

  &.typing {
    width: 2px;
    background-color: var(--primary-color);
  } 
  &.selecting {
    display: inline-block;
    background-color: var(--primary-color);
  }
}
.is-twenty{
  .custom.char{
    text-decoration: line-through;
  }
  // .lending-logo{
    // color: var(--primary-color);
    // text-decoration: line-through;
  // }
}
.title-typer{
  position: fixed;
  left:10%; 
  top: 50%;
  width: 80%;
  // transform: translate(0%,-50%);
  color:var(--bg-color);
  .lending-logo{
    font-size: 5vw;
    font-weight:700;
    font-family: $logo-font;
  }
  .vue-typer {
    .custom.char {
      font-family: $body-font;
      font-size: 2vw;
      font-weight: 400;
      // text-decoration: line-through;
    }
    .custom.char.typed {
      color: var(--bg-color);
    }
    .custom.char.selected {
      color: var(--primary-color);
    }
  }
  .custom.caret {
    animation: rocking 0.1s ease-in-out 0s infinite;
    position:absolute;
    -webkit-animation: blink 0.5s ease-in-out infinite alternate;
    -moz-animation: blink 0.5s ease-in-out infinite alternate;
    animation: blink 0.5s ease-in-out infinite alternate;
    width: 0.3vw;
    height: 2.5vw;
    &.typing {
      background-color: var(--primary-color);
    } 
    &.selecting {
      display: inline-block;
      background-color: var(--primary-color);
    }
    &.erasing {
      background-color: var(--primary-color);
    }
    &.idle {
      background-color: var(--primary-color);
    }
  }
  
}

  
@-webkit-keyframes blink{
  0% {opacity: 0;}
  100% {opacity: 1;}
}

@-moz-keyframes blink{
  0% {opacity: 0;}
  100% {opacity: 1;}
}

@keyframes blink{
  0% {opacity: 0;}
  100% {opacity: 1;}
}

.collection-button{
  margin-top:20px;
  cursor: pointer;
  border: none;
  background-color: none;
  font-weight: 500;
  color:var(--primary-color);
  .collection-in{
    stroke:var(--button-live-text-color) ;
    fill:var(--primary-color);
  }
  .collection-out{
    stroke:var(--primary-color) ;
    fill:none;
  }
  span{
    vertical-align: middle;
  }
}
</style>
