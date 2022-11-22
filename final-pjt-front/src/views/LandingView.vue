<template>
  <div class="router-view-padding">
    <h1 class="h1">LandingView</h1>

    <div class="fullscreen z-1">
    </div>
    <iframe frameborder="0" class="fullscreen z-2"
    :src="`https://www.youtube.com/embed/99Qykqxqddc?mute=1&loop=1&autoplay=1&rel=0&controls=0&showinfo=1&disablekb=1&fs=0&modestbranding=1&playsinline=1&vq=hd1080`"
    allow="autoplay; encrypted-media" 
    allowfullscreen>
  </iframe>
  
  
  <!-- :repeat='0' = 횟수 -->
    <div frameborder="0" @mousemove="mouseMove" class="fullscreen z-3">
      <div :class="isTwenty">
      </div>
    </div>
    <div frameborder="0" @mousemove="mouseMove" class="fullscreen z-4">
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
  data() {
    return {
      test:null,
      numbering:0,
      mainText:[
        '20글자까지만 입력됩니다.',
        '내 영화 리뷰 정보로 영화추천받기',
        '20글자를 넘는 영화 리뷰는 필요없어요!',
        '클릭하여 시작하세요.',
      ],
      isTwenty:"title-typer",
    }
  },
  components:{
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
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
        console.log("pageX: ",event.pageX, 
        "pageY: ", event.pageY, 
        "clientX: ", event.clientX, 
        "clientY:", event.clientY)
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


</style>