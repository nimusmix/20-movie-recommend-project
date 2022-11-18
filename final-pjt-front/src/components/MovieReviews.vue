<template>
  <div>
    <h1>MovieReviews</h1>
    <div v-for="review in reviews" :key="review.id">
      <FeedItem :review="review"/>
    </div>
    <!-- {{ reviews }} -->
  </div>
</template>

<script>
import FeedItem from '@/components/FeedItem'

export default {
  name: 'MovieReviews',
  components: {
    FeedItem,
  },  
  data(){
    return{
    }
  },
  props:{
    reviews:Array
  },
  methods:{
    getReviews(){
      
    }
  },
  created(){
    this.getReviews()
  }
}
</script>

<style>
</style>