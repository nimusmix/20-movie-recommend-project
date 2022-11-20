<template>
  <div>
    <h3 class="h3">내 리뷰</h3>
    <div v-for="review in myReviews" :key="review.id">
      <FeedItemVue :review="review"/>
    </div>
  </div>
</template>

<script>
import FeedItemVue from '@/components/FeedItem.vue'

export default {
  name: 'ReviewList',
  components: {
    FeedItemVue,
  },
  computed:{
    myReviews() {
      const myReviews = this.$store.state.reviews.filter((review) => {
        if (review.username === this.$store.state.username){
          return true
        }
        return false
      })
      return myReviews
    }
  }

}
</script>

<style>

</style>