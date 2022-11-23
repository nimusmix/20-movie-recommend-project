<template>
  <div>
    <h3 class="h3">{{ this.$route.params.username }}님의 리뷰</h3>
    <div v-if="myReviews.length">
      <div v-for="review in myReviews" :key="review.id">
        <FeedItemVue :review="review"/>
      </div>
    </div>
    <div v-else>아직 작성한 리뷰가 없습니다.</div>
  </div>
</template>

<script>
import FeedItemVue from '@/components/FeedItem.vue'

export default {
  name: 'ReviewList',
  props: {
    profileUser: Object,
  },
  components: {
    FeedItemVue,
  },
  computed:{
    myReviews() {
      const myReviews = this.$store.state.reviews.filter((review) => {
        if (review.username === this.profileUser?.username){
          return true
        }
      })
      return myReviews
    }
  }

}
</script>

<style>

</style>