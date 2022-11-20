<template>
  <div>
    <div class="feed-item" >
      <!-- {{ review }} -->
      <img class="cusor-pointer" :src="`https://image.tmdb.org/t/p/original/${ review.movie_poster_path }`" 
        @click="pushMovie"
        alt=""/>
      <!-- <div>{{ review.movie }}</div> -->
      <div class="feed-item-contents">
        <div>
          <div class="feed-item-name cusor-pointer">{{ review.username }}</div>
          <div class="feed-item-lasttime">{{ review.last_time }}</div>
        </div>
        <div class="cusor-pointer" @click="pushMovie">{{ review.movie_title }}</div>
        <!-- <div>{{ review.user }}</div> -->
        <div><span v-if="!isSpoiler">{{ review.content }}</span><span v-else style="background-color:aqua;cursor: pointer;" @click="switchIsSpoiler">스포일러방지!</span></div>
        <div style="display:inline-block">
          <b-form-rating class="star-rating" size="lg" :value="review.score"></b-form-rating> 
        </div>
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
    },
    pushMovie(){
      this.$store.dispatch("putPreference", this.review.movie)
      // putPreference()
      this.$router.push({ name: 'DetailView', params: { pk: this.review.movie }}) 
    },
    pushProfile(){

    },
  },
  created(){
    this.isSpoiler = this.review.is_spoiler
  }
}
</script>

<style>

</style>