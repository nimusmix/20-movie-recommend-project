<template>
  <div class="router-view-padding">
    <h1 class="h1">홈</h1>
    {{ recommendMovie?.title }}
    <HomeRecommend/>
    <HomeFeed/>
  </div>
</template>

<script>
import _ from 'lodash'
import HomeFeed from '@/components/HomeFeed'
import HomeRecommend from '@/components/HomeRecommend'

export default {
  name: 'HomeView',
  components: {
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
  },
  methods: {
    getRecommendMovie() {
      const recommendMovie = _.sample(this.recommendList)
      this.recommendMovie = recommendMovie
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

<style>

</style>