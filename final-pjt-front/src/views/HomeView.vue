<template>
  <div class="h1">
    <h1>홈</h1>
    <HomeRecommend/>
    <HomeFeed/>
  </div>
</template>

<script>
import HomeRecommend from '@/components/HomeRecommend'
import HomeFeed from '@/components/HomeFeed'

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