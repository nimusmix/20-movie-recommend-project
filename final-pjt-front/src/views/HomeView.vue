<template>
  <div>
    <div class="home-video-box">
      <iframe frameborder="0" class="home-video"
      :src="videoUrl"
      allow="autoplay; encrypted-media"
      allowfullscreen></iframe>

      <div v-if="recommendMovie" class="home-video-text cusor-pointer" @click="goToDetail(recommendMovie)">
        <div style="height: 80px;"></div>
        <div class="d-flex">
          <div style="width: 100px;"></div>
          <div class="home-video-title">{{ recommendMovie?.title }}</div>
        </div>
        <div class="d-flex">
          <div style="width: 100px;"></div>
          <div style="font-size: 1rem; font-weight: 300;">{{ loginUser.username }}님을 위한 추천 영화</div>
        </div>
      </div>
    </div>
    
    <div class="home-content-box">
      <div class="home-review-box">
        <h3 class="box-title">최근 20 리뷰</h3>
          <article v-for="review in recent2Reviews" :key="review.id">
            <FeedItem :review="review" style="width: 480px;"/>
          </article>
      </div>

      <div class="home-movie-box">
        <h3 class="box-title">내가 좋아할 만한 영화</h3>
        <div class="d-flex">
          <article v-for="movie in cuttedList" :key="movie.id">
            <MovieItem :movie="movie" style="width: 200px;"/>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import FeedItem from '@/components/FeedItem'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'HomeView',
  components: {
    FeedItem,
    MovieItem,
  },
  data() {
    return {
      recommendBaseList: [
        {
          name: 'similar',
          url: 'api/v1/recommend/similar',
        },
        {
          name: 'latent',
          url: 'api/v1/recommend/latent',
        },
        {
          name: 'preference',
          url: 'api/v1/recommend/preference',
        }
      ],
      recommendMovie: null,
    }
  },
  computed: {
    loginUser() {
      return this.$store.state.loginUser
    },
    recommendList() {
      let tmpList = []

      if (this.$store.state.recommendSimilar[0]) {
        tmpList.push(this.$store.state.recommendSimilar[0])
      }
      if (this.$store.state.recommendSimilar[1]) {
        tmpList.push(this.$store.state.recommendSimilar[1])
      }
      if (this.$store.state.recommendLatent[0]) {
        tmpList.push(this.$store.state.recommendLatent[0])
      }
      if (this.$store.state.recommendLatent[1]) {
        tmpList.push(this.$store.state.recommendLatent[1])
      }
      return tmpList
    },
    cuttedList() {
      return this.recommendList.slice(0, 3)
    },
    recent2Reviews() {
      return this.$store.getters.recent2Reviews
    },
    videoUrl() {
      return `https://www.youtube.com/embed/${this.recommendMovie?.key}?mute=1&loop=2&autoplay=1&rel=0&controls=0&showinfo=0&disablekb=1&fs=0&modestbranding=1&playsinline=1&vq=hd1080`
    }
  },
  methods: {
    getRecommendMovie() {
      const recommendMovie = _.sample(this.recommendList)
      this.recommendMovie = recommendMovie
    },
    goToDetail(movie) {
      this.$router.push({ name: 'DetailView', params: { pk: movie.id, movie: movie } })
    }
  },
  created() {
    for (const recommendObj of this.recommendBaseList) {
      this.$store.dispatch('getRecommend', recommendObj)
    }
    this.getRecommendMovie()
    this.$store.dispatch('getSimilar')
    this.$store.dispatch('getLoginUser')
  }
}
</script>

<style lang="scss">
  .home-video-box {
    // position: relative;
    z-index: 8;
    width: 100%;

    .home-video {
      position: relative;
      width: 100%;
      height: 500px;
      background-color:rgba(0, 0, 0, 0.287); 
    }

    .home-video-text {
      position: absolute;
      z-index: 10;
      width: 1100px;
      height: 500px;
      margin-top: -508px;
      color: white;
      font-weight: 200;

      .home-video-title {
        font-size: 2rem;
        font-weight: 600;
      }
    }
  }

  .home-content-box {
    display: flex;
    padding: 56px;

    .box-title {
      font-size: 1.2rem;
      font-weight: 600;
      margin-bottom: 1rem;
    }

    .home-review-box {
      display: inline-block;
    }

    .home-movie-box {
      display: inline-block;
      margin-left: 56px;
    }
  }
</style>