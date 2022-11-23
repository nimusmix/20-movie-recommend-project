<template>
  <div>
    <div class="home-video-box">
      <iframe frameborder="0" class="home-video"
      :src="videoUrl"
      allow="autoplay; encrypted-media"
      allowfullscreen></iframe>

        <article v-for="review in recent2Reviews" :key="review.id">
          <FeedItem :review="review"/>
        </article>
    </div>
    {{ recommendMovie?.title }}
    <HomeRecommend/>
    <HomeFeed/>
  </div>
</template>

<script>
import _ from 'lodash'
import FeedItem from '@/components/FeedItem'
import HomeFeed from '@/components/HomeFeed'
import HomeRecommend from '@/components/HomeRecommend'
// import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    FeedItem,
    HomeRecommend,
    HomeFeed,
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
      tmpList.push(this.$store.state.recommendSimilar[0])
      tmpList.push(this.$store.state.recommendSimilar[1])
      tmpList.push(this.$store.state.recommendLatent[0])
      tmpList.push(this.$store.state.recommendLatent[1])
      return tmpList
    },
    recent2Reviews() {
      return this.$store.getters.recent2Reviews
    },
    videoUrl() {
      return `https://www.youtube.com/embed/${this.recommendMovie?.key}?mute=1&loop=1&autoplay=1&rel=0&controls=0&showinfo=1&disablekb=1&fs=0&modestbranding=1&playsinline=1&vq=hd1080`
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
    // position: absolute;
    width: 100%;

    .home-video {
      position: relative;
      width: 100%;
      height: 500px;
      background-color:rgba(0, 0, 0, 0.287); 
    }

    .home-review {
      position: absolute;
      z-index: 10;
      width: 200px;
      margin-top: -200px;
    }
  }

</style>