<template>
  <div class="feed-item">
    <img class="cusor-pointer" :src="`https://image.tmdb.org/t/p/original/${ review.movie_poster_path }`" 
      @click="pushMovie"
      alt=""/>

    <div class="feed-item-contents d-flex justify-content-between">
      <div>
        <div class="feed-item-name cusor-pointer" @click="goToProfile(`${review.username}`)">{{ review.username }}</div>
        <div class="cusor-pointer mt-1" @click="pushMovie"><b>{{ review.movie_title }}</b></div>

        <div>
          <span v-if="!isSpoiler">{{ review.content }}</span>
          <span v-else class="spoiler-button" @click="switchIsSpoiler">스포일러가 포함된 리뷰입니다.</span>
        </div>
        
        <div style="display:inline-block">
          <b-form-rating class="star-rating" size="lg" :value="review.score"></b-form-rating> 
        </div>
      </div>
      <div class="feed-item-lasttime">{{ review.last_time }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FeedItem',
  data(){
    return {
      isSpoiler: true,
    }
  },
  props:{
    review: Object,
  },
  methods:{
    switchIsSpoiler(){
      if (this.isSpoiler) {
        this.isSpoiler = false
      }
    },
    pushMovie() {
      this.$store.dispatch("putPreference", this.review.movie)
      // putPreference()
      this.$router.push({ name: 'DetailView', params: { pk: this.review.movie }}) 
    },
    goToProfile(username) {
      this.$router.push({ name: 'ProfileView', params: { username: username }})
    },
  },
  created() {
    this.isSpoiler = this.review.is_spoiler
  }
}
</script>

<style>
  .spoiler-button {
    position: relative;
    z-index: 0;
    padding: 4px;
    background-color: var(--primary-color);
    color: white;
    cursor: pointer;
  }
</style>