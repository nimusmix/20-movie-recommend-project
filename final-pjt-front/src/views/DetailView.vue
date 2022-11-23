<template>
  <div>
    <div class="backdropBox">
      <img :src="backdropUrl" class="backdropImg">
    </div>

    <div class="content-box">
      <div class="movie-box">
        <img style="border-radius:8px" :src="posterUrl" class="poster-img">
        <div class="detail-box">
          <div class="movie-title">{{ movie?.title }}</div>
          <div class="details">
            <div class="detail">{{ movie?.release_date.substring(0, 4) }}</div>
            <p class="detail">·</p>
            <div class="detail" v-for="genre in this.genreList" :key="genre.id">{{ genre }}</div>
          </div>
          <div style="font-weight:500">평균 별 {{ movie?.vote_average }}</div>
          <div class="collection-button">
            <div class="selected collection-in" id="collectBtn" @click="collect" v-if="isCollected">
            <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.8198 2H7.17982C5.04982 2 3.31982 3.74 3.31982 5.86V19.95C3.31982 21.75 4.60982 22.51 6.18982 21.64L11.0698 18.93C11.5898 18.64 12.4298 18.64 12.9398 18.93L17.8198 21.64C19.3998 22.52 20.6898 21.76 20.6898 19.95V5.86C20.6798 3.74 18.9498 2 16.8198 2Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M9.58984 11L11.0898 12.5L15.0898 8.5"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              
            </svg>
            <span>
              내 컬렉션
                </span>
            </div>
            <div class="collection-out" id="collectBtn" @click="collect" v-else>
            <svg  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M16.8198 2H7.17982C5.04982 2 3.31982 3.74 3.31982 5.86V19.95C3.31982 21.75 4.60982 22.51 6.18982 21.64L11.0698 18.93C11.5898 18.64 12.4298 18.64 12.9398 18.93L17.8198 21.64C19.3998 22.52 20.6898 21.76 20.6898 19.95V5.86C20.6798 3.74 18.9498 2 16.8198 2Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M14.5 10.65H9.5M12 8.20996V13.21"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
                <span>
                  내 컬렉션에 추가하기
                </span>
            </div>
          </div>
        </div>
      </div>
      <div class="space"></div>      
      <div class="overview-box">
        <h3 class="h3">줄거리</h3>
        <p>{{ movie?.overview }}</p>
      </div>
      
      <div class="space"></div>
      <ReviewCreate @review-created="reviewCreated"/>
      <div class="space"></div>
      <MovieReviews :reviews="reviews"/>
      <div class="space"></div>
      <MovieCollections :movie="movie"/>
    </div>
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
      this.genreList = []
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

          const imgUrl = 'https://image.tmdb.org/t/p/original/'
          this.backdropUrl = imgUrl + this.movie.backdrop_path
          this.posterUrl = imgUrl + this.movie.poster_path

          if (this.loginUser.collection.includes(this.movie?.id)) {
            this.isCollected = true
          } else {
            this.isCollected = false
          }
        })
        .then(() => {
          this.getReviews()
        })
        .catch(() => {
          this.$router.push('/404')
        })
    },

    getReviews() {
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
    },

    collect() {
      this.isCollected = !this.isCollected
      
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v3/accounts/collect/${this.movie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.$store.dispatch('getLoginUser')
          if (this.isCollected) {
            alert('내 컬렉션에 추가했습니다.')
          } else {
            alert('내 컬렉션에서 제외했습니다.')
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },

    reviewCreated() {
      this.getMovie()
    }
  },
  created() {
    this.getMovie()
  },
}
</script>

<style lang="scss">
  .backdropBox {
    position: relative;
    // background-color: black;
    height: 400px;
    overflow: hidden;

    .backdropImg {
      position: absolute;
      top: 50%;
      width: 100%;
      opacity: 70%;
      transform: translate(0%, -50%);
    }
  }

  .content-box {
    margin: 56px;

    .movie-box {
      display: flex;

      .movie-title {
        font-size: 2rem;
        font-weight: 600;
      }
    
      .poster-img {
        width: 200px;
        height: auto;
      }
    
      .detail-box {
        margin-left: 24px;
    
        .details {
          display: flex;
    
          .detail {
            margin-right: 5px;
          }
        }
      }
    }

    .overview-box {
      
      p {
        margin: 0;
      }
    }
  }
</style>