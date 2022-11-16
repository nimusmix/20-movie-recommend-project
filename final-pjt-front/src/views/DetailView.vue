<template>
  <div>
    <h1>DetailView</h1>
    <ReviewCreate/>
    <MovieReviews :movie="movie"/>
    <MovieCollections/>
    {{ movie }}
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
  props:{
    movie:Object
  }
}
</script>

<style>

</style>