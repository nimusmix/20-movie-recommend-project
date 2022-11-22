<template>
  <div>
    <h3 class="h3">다른 사용자의 리뷰</h3>
    <div v-for="review in reviews" :key="review.id">
      <FeedItem :review="review"/>
    </div>
  </div>
</template>

<script>
import FeedItem from '@/components/FeedItem'

export default {
  name: 'MovieReviews',
  components: {
    FeedItem,
  },  
  props: {
    reviews: Array
  },
}
</script>

<style>
</style>