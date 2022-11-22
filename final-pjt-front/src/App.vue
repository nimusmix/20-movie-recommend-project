<template>
  <div id="app" :class="mainclass">

      <nav id="col-nav">
        <div id="nav-logo" class="logo t-d-none cusor-pointer" @click="goToHome">20.</div>

        <div id="nav-profile-box">
          <div id="nav-profile-img-box" class="cusor-pointer inner-shadow">
            <img class="img-circle-80" v-if="loginUser?.profile_img" :src="`http://127.0.0.1:8000${loginUser?.profile_img}`" @click="goToProfile">
            <img class="img-circle-80" v-else src="@/assets/basic.png" @click="goToProfile">
          </div>
          <div style="height: 0.4rem;"></div>
          <router-link :to="{ name: 'ProfileView', params: { username: loginUser?.username } }">{{ loginUser?.username }}</router-link>
        </div>

        <div v-if="isLogin">
          <button @click="logout">로그아웃</button>
        </div>

        <ul id="nav-ul">
          <div v-if="!isLogin">
            <li
              v-for="(routerName, routerLink, index) in loginLinks" :key="index"
            >
              <div class="li-inner-box cusor-pointer" @click="goToLink(routerLink)">
                <router-link class="nav-item" :to="{ name: routerLink }" >
                  <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M1.52 16.11H20.48M1.52 6.11H20.48M5.97 16.11V20.46M11 16.11V20.97M15.97 16.11V20.52M5.97 1.11V5.46M11 1.11V5.97M11 6.03V17.03M15.97 1.11V5.52M21 14V8C21 3 19 1 14 1H8C3 1 1 3 1 8V14C1 19 3 21 8 21H14C19 21 21 19 21 14Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                  <div class="v-a-middle">
                    {{ routerName }}
                  </div>
                </router-link>
              </div>
            </li>
          </div>

          <li 
          v-for="(routerName, routerLink, index) in routerLinks" :key="index"
          >
            <div class="li-inner-box cusor-pointer" @click="goToLink(routerLink)">
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
          {{ width }} 
          {{ height }}
        </ul>
        <button @click="changeClass">변경하기</button>

      </nav>
      <router-view id="router-view"/>
  </div>
</template>
<script>
  export default {
    data() {
      return{
        mainclass:'light',
        loginLinks: {
          'LoginView': '로그인',
          'SignupView': '회원가입'
        },
        routerLinks: {
          'LandingView': '랜딩페이지',
          'HomeView': '홈',
          'FeedView': '피드',
          'RecommendView': '추천영화',
          'CategoryView': '카테고리'
        },
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

  $logo-font: 'Unna', serif;  // 순위2
  // $logo-font: 'Manrope', sans-serif;  //순위1
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
    --text-color-0:#0000;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;

    //피드 및 네비 그림자
    --feed-shadow:rgba(0, 0, 0, 0.03);

    //프로필 이미지 외곽선
    --img-border:rgba(0, 0, 0, 0.05);
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
    --text-color-0:#FFF0;

    //버튼 텍스트 컬러
    --button-live-text-color:#FFF;
    
    //피드 그림자
    --feed-shadow:rgb(255, 255, 255, 0.01);

    //프로필 이미지 외곽선
    --img-border:rgba(255, 255, 255, 0.05);
  }
// 텍스트 스타일
  // 큰 텍스트 - h1
  $lg-font-size:2rem;
  $lg-font-weight:600;

  // 일반 텍스트 - 기본
  $main-font-size:1.0rem;
  $main-font-weight:400;

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
    box-shadow: inset 4px 4px 15px rgba(0, 0, 0, 0.05);
  }

  // 전역설정
  #app .h1 {
    font-size: $lg-font-size;
    font-weight: $lg-font-weight;
    margin-bottom: 24px;
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
$shadow-primary: 0px 0px 10px 0px var(--primary-color-15);

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
      box-shadow: $shadow-primary;
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
    font-weight: 600;
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
    margin-left: $nav-width;
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
    height: 5px;
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
    font-weight: 900;
    top:50%;
    transform: translate(0%,-50%);
    border-radius: 50%;
    color: var(--bg-color);
    background-color: var(--text-color-80);
    transition: left 0.1s, right 0.1s, width 0.5s, height 0.4s, border-radius 0.5s, background-color 0.5s, transform 0.5s, border-color 0.5s, color 0.5s, box-shadow 0.5s;
    box-shadow: $shadow-default;
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

    a {
      color: var(--text-color);

      img {
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
    border: 1px solid var(--text-color);
    padding: 1rem 1.5rem ;
    background: var(--bg-color);
    border-radius: 8px;
    border-color: var(--primary-color);
    box-shadow: $shadow-primary;

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
    z-index: 2;
    background-color: black;
  }

  .modal-card{
   -ms-overflow-style: none;
  }


  .modal-card {
    /* position: relative; */
    /* height: 70%; */
    position: fixed;
    width: 70%;
    /* position: absolute; */
    top: 50%;
    left: 15%;
    transform: translate(0%,-50%);
    
    margin-left: auto;
    margin-right: auto;
    z-index: 3;
    /* overflow:scroll; */
    padding: 20px;
    background-color: white;
    /* border: 1px red solid; */
  }

  .modal-movie{
    width: 200px;
  }

  .center-head{
    display: flex;
    justify-content: center;
    margin: 2rem 0px;
  }
</style>
