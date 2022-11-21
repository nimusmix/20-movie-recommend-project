<template>
  <div class="router-view-padding">
    <h1 class="h1">피드</h1>
    <article v-for="review in reviews" :key="review.id">
      <FeedItem :review="review"/>
    </article>
  </div>
</template>

<script>

import FeedItem from '@/components/FeedItem'


export default {
  name: 'FeedView',
  components: {
    FeedItem,
  },  
  methods: {
    // getReviews() {
    //   this.$store.dispatch('getReviews')
    // },
  },
  computed:{
    reviews(){
      return this.$store.state.reviews
    }
  },
  // created() {
  //   this.getReviews()
  // },

}
</script>

<style>

</style>