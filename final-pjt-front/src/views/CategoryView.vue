<template>
  <div>
    <h1>CategoryView</h1>
    <CategoryItem/>
    {{ movies }}
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