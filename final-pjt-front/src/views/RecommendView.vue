<template>
  <div class="router-view-padding">
    
    <h1 class="h1">{{ username }}님과 비슷한 사용자들이 좋아하는 영화입니다.</h1>
    <!-- <div class="row-scroll mb-5">
      <article 
        v-for="movie in recommendSimilar"
        :key="movie.id"
        class="col row-scroll-item"
      >
        <MovieItem :movie="movie"/>
      </article>
    </div> -->

    <div style="position:relative">
      <button @click="scrollRight('recommendSimilar')" class="row-scroll-button r-s-b-left">{{ leftIcon }}</button>
      <button @click="scrollLeft('recommendSimilar')" class="row-scroll-button r-s-b-right">{{ rightIcon }}</button>
      <div class="row-scroll mb-5" :ref="'recommendSimilar'" >
        <article 
          v-for="movie in recommendSimilar"
          :key="movie.id"
          class="col row-scroll-item"
          >
          <MovieItem :movie="movie" class="modal-movie"/>
        </article>
      </div>
    </div>

    <!-- 잠재 모델 -->
    <h1 class="h1">{{ username }}님이 좋아할 만한 영화입니다.</h1>

    <div style="position:relative">
      <button @click="scrollRight('recommendLatent')" class="row-scroll-button r-s-b-left">{{ leftIcon }}</button>
      <button @click="scrollLeft('recommendLatent')" class="row-scroll-button r-s-b-right">{{ rightIcon }}</button>
      <div class="row-scroll mb-5" :ref="'recommendLatent'" >
        <article 
          v-for="movie in recommendLatent"
          :key="movie.id"
          class="col row-scroll-item"
          >
          <MovieItem :movie="movie" class="modal-movie"/>
        </article>
      </div>
    </div>

    <!-- 선호 장르 -->
    <h1 class="h1">{{ Object.keys(recommendPreference)[0] }}</h1>
    <div style="position:relative">
      <button @click="scrollLeft(`'prefer1'${0}`)" class="row-scroll-button r-s-b-left">{{ leftIcon }}</button>
      <button @click="scrollLeft(`'prefer1'${0}`)" class="row-scroll-button r-s-b-right">{{ rightIcon }}</button>
      <div class="row-scroll mb-5" :ref="`'prefer1'${0}`" >
        <article 
          v-for="movie in recommendPreference[Object.keys(recommendPreference)[0]]"
          :key="movie.id"
          class="col row-scroll-item"
          >
          <MovieItem :movie="movie" class="modal-movie"/>
        </article>
      </div>
    </div>
    <h1 class="h1">{{ Object.keys(recommendPreference)[1] }}</h1>
    <div style="position:relative">
      <button @click="scrollLeft(`'prefer1'${1}`)" class="row-scroll-button r-s-b-left">{{ leftIcon }}</button>
      <button @click="scrollLeft(`'prefer1'${1}`)" class="row-scroll-button r-s-b-right">{{ rightIcon }}</button>
      <div class="row-scroll mb-5" :ref="`'prefer1'${1}`" >
        <article 
          v-for="movie in recommendPreference[Object.keys(recommendPreference)[1]]"
          :key="movie.id"
          class="col row-scroll-item"
          >
          <MovieItem :movie="movie" class="modal-movie"/>
        </article>
      </div>
    </div>
    <h1 class="h1">{{ Object.keys(recommendPreference)[2] }}</h1>
    <div style="position:relative">
      <button @click="scrollLeft(`'prefer1'${2}`)" class="row-scroll-button r-s-b-left">{{ leftIcon }}</button>
      <button @click="scrollLeft(`'prefer1'${2}`)" class="row-scroll-button r-s-b-right">{{ rightIcon }}</button>
      <div class="row-scroll mb-5" :ref="`'prefer1'${2}`" >
        <article 
          v-for="movie in recommendPreference[Object.keys(recommendPreference)[2]]"
          :key="movie.id"
          class="col row-scroll-item"
          >
          <MovieItem :movie="movie" class="modal-movie"/>
        </article>
      </div>
    </div>
    <!-- </div> -->
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'

export default {
  name: 'RecommendView',
  components: {
    MovieItem
  },
  data(){
    return{
      leftIcon : '<',
      rightIcon : '>',
      genres : [],
    }
  },
  methods: {
    scrollRight(idx){
      const move = parseInt(this.$store.state.width / 2)
      this.$refs[idx].scrollBy({ left: -move, behavior: 'smooth' });
    },
    scrollLeft(idx){
      const move = parseInt(this.$store.state.width / 2)
      this.$refs[idx].scrollBy({ left: move , behavior: 'smooth' });
    },
  },
  computed: {
    recommendSimilar() {
      return this.$store.state.recommendSimilar
    },
    recommendLatent() {
      return this.$store.state.recommendLatent
    },
    recommendPreference() {
      return this.$store.state.recommendPreference
    },
    username() {
      return this.$store.state.username
    },
    
  },
  watch: {
    // keyss() {
    //   return this.recommendPreference.keys()
    // }
  }
}
</script>

<style lang="scss">
  
</style>