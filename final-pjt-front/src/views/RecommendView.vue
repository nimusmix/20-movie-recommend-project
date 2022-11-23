<template>
  <div class="router-view-padding">
    <h1 class="h1"  v-if="recommendSimilar.length">{{ username }}님과 비슷한 사용자들이 좋아하는 영화입니다.</h1>

    <div style="position:relative" v-if="recommendSimilar.length">
      <button @click="scrollRight('recommendSimilar')" class="row-scroll-button r-s-b-left">
        <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button @click="scrollLeft('recommendSimilar')" class="row-scroll-button r-s-b-right">
        <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
      </button>
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
      <button @click="scrollRight('recommendLatent')" class="row-scroll-button r-s-b-left">
        <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button @click="scrollLeft('recommendLatent')" class="row-scroll-button r-s-b-right">
        <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
      </button>
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
      <button @click="scrollRight(`'prefer1'${0}`)" class="row-scroll-button r-s-b-left">
        <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button @click="scrollLeft(`'prefer1'${0}`)" class="row-scroll-button r-s-b-right">
        <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
      </button>
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
      <button @click="scrollRight(`'prefer1'${1}`)" class="row-scroll-button r-s-b-left">
        <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button @click="scrollLeft(`'prefer1'${1}`)" class="row-scroll-button r-s-b-right">
        <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
      </button>
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
      <button @click="scrollRight(`'prefer1'${2}`)" class="row-scroll-button r-s-b-left">
        <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>
      <button @click="scrollLeft(`'prefer1'${2}`)" class="row-scroll-button r-s-b-right">
        <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
      </button>
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
    return {
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
  created() {
    // for (const recommendObj of this.recommendBaseList) {
    //   this.$store.dispatch('getRecommend', recommendObj)
    // }
  }
}
</script>

<style lang="scss">
  
</style>