<template>
  <div class="router-view-padding">
    <h1 class="h1">홈</h1>
    <HomeRecommend/>
    <HomeFeed/>
  </div>
</template>

<script>
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
    }
  },
  created() {
    for (const recommendObj of this.recommendBaseList) {
      this.$store.dispatch('getRecommend', recommendObj)
    }
  }
}
</script>

<style>

</style>