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
  }
}
</script>

<style>

</style>