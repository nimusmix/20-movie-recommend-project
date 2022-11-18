<template>
  <div>
    <h1 class="h1">{{ movie?.title }}</h1>
    <div @click="collect">
      <button id="collectBtn" v-if="isCollected">콜렉션에서 빼기</button>
      <button id="collectBtn" v-else>콜렉션에 넣기</button>
    </div>
    <p>{{ isCollected }}</p>
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
      isCollected: false,
    }
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
    loginUser() {
      return this.$store.state.loginUser
    },
  },
  methods: {
    getMovie() {
      // 개별 영화정보를 받아오기 위한 axios
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
      })
      .then(() => {
        // 리뷰를 받아오기 위한 axios
        axios({
          method: 'get',
          url: `${this.$store.state.API_URL}/api/v2/movies/${this.movie.id}/get-reviews/`,
        })
        .then((res) => {
          console.log('detailView의 get-reviews 성공!')
          this.reviews = res.data.review_set.reverse()
        })
        .catch(() => {
          console.log('detailView의 get-reviews 실패!')
        })
        // 로그인한 사용자의 colletion에 해당 영화가 존재하는지 여부를 판단
        .then(() => {
          if (this.loginUser.collection.includes(this.movie.id)) {
            this.isCollected = true
          }
        })
      })
      .catch((err) => {
        console.log(err)
      })
    },
    collect() {
      this.isCollected = !this.isCollected
      if (this.isCollected) {
        axios({
          method: 'put',
          url: `${this.$store.state.API_URL}/api/v3/accounts/${this.loginUser.username}/collect`,
          data: {
            username: this.loginUser.username,
            collection: this.movie.id,
          }
        })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        // 아직 구현 안함..
        // axios delete로 구현하면 될 듯!
      }
    },
  },
  created() {
    this.getMovie()
  }
}
</script>

<style>

</style>