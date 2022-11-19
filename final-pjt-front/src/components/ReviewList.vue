<template>
  <div>
    <h1>ReviewList</h1>
    <ReviewListItem/>
    <div v-for="review in myReviews" :key="review.id">
      <FeedItemVue :review="review"/>
    </div>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import FeedItemVue from '@/components/FeedItem.vue'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
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