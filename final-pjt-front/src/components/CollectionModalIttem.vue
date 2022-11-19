<template>
  <div>
    <!-- <div class="movie-card">
    <router-link class="t-d-none" :to="{ name: 'DetailView', params: { pk: movie.id, movie:movie }}">
      <img :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
      class="card-img-top" alt="...">
      <h5>{{ movie.title }}</h5>
      <p><span>평균 별 </span>{{ movie.vote_average }}</p>
    </router-link>
    </div> -->
    <h2>모달 아이템임..</h2>
  </div>
</template>

<script>
export default {
  name: 'CollectionModalItem',
  // props: {
  //   movie: Object,
  // }
}
</script>

<style>
</style>