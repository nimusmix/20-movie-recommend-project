<template>
  <div class="movie-card">
    <div class="logos">
      <img src="@/assets/watcha.jpg" class="img-circle-ott" v-if="servingOtts.includes(97)">
      <img src="@/assets/waave.png" class="img-circle-ott" v-if="servingOtts.includes(356)">
      <img src="@/assets/disney.jpg" class="img-circle-ott" v-if="servingOtts.includes(337)">
      <img src="@/assets/netflix.png" class="img-circle-ott" v-if="servingOtts.includes(8)">
    </div>
    <a class="t-d-none" @click.prevent="putPreference()">
      <div>
        <img :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
        class="card-img-top" alt="...">
      </div>
      <h5 class="movie-card-title">{{ movie.title }}</h5>
      <div class="movie-card-detail">{{ movie?.release_date.substring(0, 4) }}</div>
      <p class="movie-card-detail"><span>평균 별 </span>{{ movie.vote_average }}</p>
    </a>

  </div>
</template>
  
<script>
  export default {
    name: 'MovieItem',
    props:{
      movie: Object,
    },
    methods:{
      putPreference() {
        const genres = this.movie.genres
        for (const genre of genres) {
          this.$store.dispatch('putPreference', genre)
        }
        this.$router.push({ name: 'DetailView', params: { pk: this.movie.id, movie: this.movie } })
      },
    },
    computed: {
      servingOtts() {
        return Object.values(this.movie.otts)
      }
    },
  }
</script>
  
<style lang="scss">
  .logos {
    position: absolute;
    z-index: 3;
    margin: 5px;
    // margin-left: auto;
    // margin-right: auto;

    img {
      margin: 1.2px;
    }
  }
</style>