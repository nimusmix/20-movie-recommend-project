<template>
  <div>
    <div class="row row-cols-1 row-cols-md-4
         g-4">
      <article 
      v-for="(movie, index) in movies"
      :key="index"
      class="col"
      >
      <CategoryItem :movie="movie"/>
    </article>
    </div>
    
  </div>
</template>

<script>
import CategoryItem from '@/components/CategoryItem'

export default {
  name: 'CategoryView',
  components: {
    CategoryItem,
  },
  computed:{
    movies(){
      return this.$store.state.movies
    }
  }
}
</script>

<style>

</style>