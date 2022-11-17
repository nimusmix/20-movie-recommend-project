<template>
  <div>
    <h1>FeedView</h1>
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
    getReviews() {
      this.$store.dispatch('getReviews')
    },
  },
  computed:{
    reviews(){
      return this.$store.state.reviews
    }
  },
  mounted() {
    this.getReviews()
  },

}
</script>

<style>

</style>