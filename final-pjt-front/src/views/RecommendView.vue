<template>
  <div>
    <h1>RecommendView</h1>
    <RecommendSimilar/>
    <RecommendGenre/>
    <RecommendRecentlyReview/>
  </div>
</template>

<script>
import RecommendSimilar from '@/components/RecommendSimilar'
import RecommendGenre from '@/components/RecommendGenre'
import RecommendRecentlyReview from '@/components/RecommendRecentlyReview'

export default {
  name: 'RecommendView',
  components: {
    RecommendSimilar,
    RecommendGenre,
    RecommendRecentlyReview,
  }
}
</script>

<style>

</style>