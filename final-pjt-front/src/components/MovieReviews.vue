<template>
  <div>
    <h3 class="h3">리뷰 목록</h3>
    <div v-if="reviews?.length">
      <div v-for="review in reviews" :key="review.id">
        <FeedItem :review="review"/>
      </div>
    </div>
    <div v-else>작성된 리뷰가 없습니다.</div>
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