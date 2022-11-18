<template>
  <div>
    <h1 class="h1">{{ movie?.title }}</h1>
    <div style="background-color: white;">
      <img :src="backdropUrl" alt="background" style="width: 100%; opacity: 70%;">
    </div>
    <img :src="posterUrl" alt="poster">
    <div>{{ movie?.title }}</div>
    <div>{{ movie?.release_date.substring(0, 4) }}</div>

    <div>
      <div>줄거리</div>
      <p>{{ movie?.overview }}</p>
    </div>

    <div>{{ movie?.vote_average }}</div>
    <div v-for="genre in this.genreList" :key="genre.id">{{ genre }}</div>
    <ReviewCreate/>
    <MovieReviews :reviews="reviews"/>
    <MovieCollections/>
  </div>
</template>

<script>
import axios from 'axios'

import ReviewCreate from '@/components/ReviewCreate'
import MovieReviews from '@/components/MovieReviews'
import MovieCollections from '@/components/MovieCollections'

export default {
  name: 'DetailView',
  components: {
    ReviewCreate,
    MovieReviews,
    MovieCollections,
  },
  data() {
    return {
      movie: null,
      genreList: [],
      backdropUrl: null,
      posterUrl: null,
      reviews: null,
    }
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
  },
  methods: {
    getMovie() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.$route.params.pk}/`
      })
        .then((res) => {
          this.movie = res.data
          this.movie.genres.forEach((genre) => {
            for (const genreObj of this.genres) {
              if (genreObj.id === genre) {
                this.genreList.push(genreObj.name)
              }
            }
          })
          const imgUrl = 'https://image.tmdb.org/t/p/w500/'
          this.backdropUrl = imgUrl + this.movie.backdrop_path
          this.posterUrl = imgUrl + this.movie.poster_path
        }).then(() => {
          axios({
            method: 'get',
            url: `${this.$store.state.API_URL}/api/v2/movies/${this.movie.id}/get-reviews/`,
          })
            .then((res) => {
              console.log('actions의 get-reviews 성공!')
              this.reviews = res.data.review_set.reverse()
            })
            .catch(() => {
              console.log('actions의 get-reviews 실패!')
            })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getMovie()
  }
}
</script>

<style>

</style>