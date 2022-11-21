<template>
    <div class="movie-card" >
      <a class="t-d-none" @click.prevent="putPreference()" >
        <img :src="`https://image.tmdb.org/t/p/original/${ movie.poster_path }`" 
        class="card-img-top" alt="...">
        <h5 class="movie-card-title">{{ movie.title }}</h5>
        <div class="movie-card-detail">{{ movie?.release_date.substring(0, 4) }}</div>
        <p class="movie-card-detail"><span>평균 별 </span>{{ movie.vote_average }}</p>
      </a>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MovieItem',
    props:{
      movie:Object
    },
    methods:{
      putPreference(){
        const genres = this.movie.genres
        for (const genre of genres){
          this.$store.dispatch('putPreference', genre)
        }
        this.$router.push({ name: 'DetailView', params: { pk: this.movie.id, movie: this.movie }}) 
      }
    }
  }
  </script>
  
  <style>
  
  </style>