<template>
  <div class="card">
    <router-link :to="{ name: 'DetailView', params: { pk: movie.id, movie:movie }}">
      <img :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
      class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.vote_average }}</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'CategoryItem',
  props:{
    movie:Object
  }
}
</script>

<style>

</style>