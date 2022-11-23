<template>
  <div class="router-view-padding" @mousemove="mouseMove" >
    <h1 class="h1">LandingView</h1>

    <div class="fullscreen z-1">
    </div>
    <!-- 99Qykqxqddc -->
    <iframe frameborder="0" class="fullscreen z-2"
    
      :src="`https://www.youtube.com/embed/toGEheu4eq4?mute=1&loop=1&autoplay=1&rel=0&controls=0&showinfo=1&disablekb=1&fs=0&modestbranding=1&playsinline=1&vq=hd1080`"
      allow="autoplay; encrypted-media" 
      allowfullscreen>
    </iframe>

  <div class="sub-fullscreen" :style="xyCss" >
    <router-link v-if="isLogin"  :to="{ name: 'HomeView' }">
      <div class="landing-cursor" style="">
        <div class="landing-text">들어가기</div>
      </div>
    </router-link>
    <router-link v-else  :to="{ name: 'LoginView' }">
      <div class="landing-cursor" style="">
        <div class="landing-text">들어가기</div>
      </div>
    </router-link>
    <!-- <div v-if="isLogin">
      들어가기</router-link>
    </div>
    <div v-else>
      <router-link :to="{ name: 'LoginView' }">로그인</router-link> | 
      <router-link :to="{ name: 'SignupView' }">회원가입</router-link>
    </div> -->
  </div>
  
  <!-- :repeat='0' = 횟수 -->
    <div frameborder="0" class="fullscreen z-3">
      <div :class="isTwenty">
      </div>
    </div>
    <div frameborder="0" class="fullscreen z-4">
      <div :class="isTwenty">
        <div class="lending-logo">{{ numbering }}.</div>
        <vue-typer
          :text='mainText'
          :repeat='Infinity' 
          :shuffle='false'
          initial-action='typing'
          :pre-type-delay='70'
          :type-delay='91'
          :pre-erase-delay='1500'
          :erase-delay='100'
          erase-style="select-all"
          :erase-on-complete='true'
          caret-animation="smooth"
          @typed='onTyped'
          @typed-char='onTypedChar'
        ></vue-typer>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {

  name: 'LandingView',
  data() {
    return {
      landingX:0,
      landingY:0,
      test:null,
      numbering:0,
      mainText:[
        '20글자까지만 입력됩니다.',
        '내 영화 리뷰 정보로 영화추천받기',
        '20글자를 넘는 영화 리뷰는 필요없어요!',
        '클릭하여 시작하세요.',
      ],
      isTwenty:"title-typer",
      xyCss:'',
    }
  },
  components:{
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods:{
    onTyped(e){
      this.test = e
    },
    onTypedChar(typedChar, typedCharIndex) {
        // this.mainText = this.mainText.concat(typedChar)
        this.numbering = typedCharIndex
        this.isTwenty = "title-typer"
        if (typedCharIndex > 20 ){
          this.isTwenty = "title-typer is-twenty"
        }
      },
      mouseMove(event){
        this.landingX = event.clientX 
        this.landingY = event.clientY
        this.xyCss = `z-index:9; width:200px; height:100px; top:${this.landingY}px; left:${this.landingX}px;  `
        //`background-position: px px;`
        
        console.log(
          "pageX: ",event.pageX, 
          "pageY: ", event.pageY, 
          // "clientX: ", 
          // "clientY:", 
        )
      }
  },
}
</script>

<style lang="scss">
.fullscreen{
  cursor: pointer;
  width:100vw; height:100vh; position: fixed; top:0px; left:0px;  transform: translate(0%,0%);
  background-color:rgba(0, 0, 0, 0.287); 
  &z-4{
    z-index: 4;
  }
  &z-3{
    z-index: 3;
  }
  &z-2{
    z-index: 2;
  }
  &z-1{
    z-index: 1;
  }
}
.sub-fullscreen{
  cursor: pointer;
  width:100vw; height:100vh; position: fixed; ;
}
.landing-cursor{
  border-radius:50%;
  position: relative;
  width:100px;
  height:100px;
  vertical-align: middle;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.492); 
  z-index: 15;
  transform: translate(-50%,-50%);
  
  a:hover{
    text-decoration: none;
  }
  .landing-text{
    
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    color:#FFF;
    font-size: 16px;
  }
}


</style>
