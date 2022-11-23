<template>
  <div>
    <div class="home-video-box">
      <iframe frameborder="0" class="home-video"
      :src="videoUrl"
      allow="autoplay; encrypted-media"
      allowfullscreen></iframe>

      <div class="home-video-text">
        <div class="home-video-title">{{ recommendMovie?.title }}</div>
        <p style="font-size: 1rem; font-weight: 300;">{{ loginUser.username }}님을 위한 추천 영화</p>
      </div>
    </div>
    
    <div class="content-box">
      <div class="review-box">
        <h3 class="box-title">최근 20 리뷰</h3>
          <article v-for="review in recent2Reviews" :key="review.id">
            <FeedItem :review="review" style="width: 480px;"/>
          </article>
      </div>
      <div style="width: 48px;"></div>
      <div class="movie-box">
        <h3 class="box-title">나와 비슷한 사용자들이 좋아하는 영화</h3>
        
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import FeedItem from '@/components/FeedItem'

export default {
  name: 'HomeView',
  components: {
    FeedItem,
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
        tmpList.push(this.$store.state.recommendLatent[0])
      }
      return tmpList
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
    width: 100%;

    .home-video {
      position: relative;
      width: 100%;
      height: 500px;
      // width: 140vw;
      // height: 100vh;
      // margin-top: -50vh;
      background-color:rgba(0, 0, 0, 0.287); 
    }

    .home-video-text {
      position: absolute;
      z-index: 10;
      width: auto;
      margin-top: -440px;
      margin-left: 80px;
      color: white;
      font-weight: 200;

      .home-video-title {
        font-size: 2rem;
        font-weight: 600;
      }
    }
  }

  .content-box {
    display: flex;
    padding: 56px;

    .box-title {
      font-size: 1.2rem;
      font-weight: 600;
      margin-bottom: 1rem;
    }

    .review-box {
      display: inline-block;
    }

    .movie-box {
      display: inline-block;
    }
  }

</style>