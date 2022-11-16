<template>
  <div>
    <h1>DetailView</h1>
    <ReviewCreate/>
    <MovieReviews/>
    <MovieCollections/>
  </div>
</template>

<script>
import ReviewCreate from '@/components/ReviewCreate'
import MovieReviews from '@/components/MovieReviews'
import MovieCollections from '@/components/MovieCollections'

export default {
  name: 'DetailView',
  components: {
    ReviewCreate,
    MovieReviews,
    MovieCollections,
  },
  
}
</script>

<style>

</style>