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
// const element = document.querySelector('#element');
// const effect = new TypeIt(element, {
//   strings: "This very long effect will be cancelled as soon as the user clicks in it!"
// });

// element.addEventListener('focus', () => {
//   effect.reset();
// });

// element.addEventListener('blur', (e) => {
  // effect.go();
   
// });
export default {

  name: 'LandingView',
  data(){
    return {
      effect : null,
    }
  },
  components:{
    
  },
  methods: {
    // makeTypeIt(){
    //   this.effect = new TypeIt(this.$refs.typeit, {
    //     strings: "This very long effect will be cancelled as soon as the user clicks in it!"
    //   })
    // },
    // focusTypeIt(){
    //   this.effect.reset()
    // },
    // blurTypeIt(e){
    //   if(!e.target.value.length) {
    //     this.effect.go();   
    //   }
    
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
    // this.makeTypeIt()
  }
}
</script>

<style lang="scss">
#typeIt-test {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  padding: 0 2rem;
  font-weight: 600;
}

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