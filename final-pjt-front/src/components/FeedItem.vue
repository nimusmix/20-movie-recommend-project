<template>
  <div>
    <div style="border:1px solid black">
      <!-- {{ review }} -->
      <img width="100px" :src="`https://image.tmdb.org/t/p/original/${ review.movie_poster_path }`" alt=""/>
      <!-- <div>{{ review.movie }}</div> -->
      <div style="display:inline-block">
        <div>{{ review.movie_title }}</div>
        <div>{{ review.last_time }}</div>
        <!-- <div>{{ review.user }}</div> -->
        <div>{{ review.username }}</div>
        <div><span v-if="!isSpoiler">{{ review.content }}</span><span v-else style="background-color:aqua;cursor: pointer;" @click="switchIsSpoiler">스포일러방지!</span></div>
        
        <div>{{ review.score }}</div>
      </div>
      <!-- <div>{{ review.is_spoiler }}</div>
      {{ isSpoiler }} -->
      <!-- <button @click="switchIsSpoiler">스포일러 해제</button> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  data(){
    return {
      isSpoiler:true,
    }
  },
  props:{
    review: Object,
  },
  methods:{
    switchIsSpoiler(){
      if (this.isSpoiler){
        this.isSpoiler = false
      }
    }
  },
  created(){
    this.isSpoiler = this.review.is_spoiler
  }
}
</script>

<style>

</style>