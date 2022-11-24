<template>
  <div class="feed-item">
    <img class="cusor-pointer" :src="`https://image.tmdb.org/t/p/original/${ review.movie_poster_path }`" 
      @click="pushMovie"
      alt=""/>
    
    <div class="feed-item-contents d-flex justify-content-between">
      <div style="position:relative">
        
        <div class="feed-item-name cusor-pointer" @click="goToProfile(`${review.username}`)">@{{ review.username }}</div>
        <div class="cusor-pointer mt-2" @click="pushMovie"><b>{{ review.movie_title }}</b></div>

        <div style="margin-top:4px; margin-bottom: 0px;">
          <span v-if="!isSpoiler" class="feed-nospo">{{ review.content }}</span>
          <span v-else class="spoiler-button" @click="switchIsSpoiler">스포일러가 포함된 리뷰입니다.</span>
        </div>
        
        <!-- 별점 -->
        <div style="position:absolute; width: 120px; bottom: 0px;">
          <div v-for="idx of 5" :key="idx" style="display:inline-block; margin-right: 4px;">
            <div v-if="idx <= review.score">
              <svg  viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" aria-label="star fill" xmlns="http://www.w3.org/2000/svg" fill="#FF715E" class="bi-star-fill b-icon bi">
                <g class=""> 
                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z">
                </path>
                </g>
              </svg>
            </div>
            <div v-else>
              <svg  viewBox="0 0 16 16" width="1em" height="1em" focusable="false" role="img" aria-label="star fill" xmlns="http://www.w3.org/2000/svg" stroke="#FF715E" fill="none" class="bi-star-fill b-icon bi">
                <g class=""> 
                <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z">
                </path>
                </g>
              </svg>
            </div>
          </div>
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
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  methods:{
    switchIsSpoiler(){
      if (this.isSpoiler) {
        this.isSpoiler = false
      }
    },
    pushMovie() {
      const movie = this.movies.find((movie) => {return movie.id === this.review.movie})
      for (const genre of Object.values(movie.genres)) {
        this.$store.dispatch("putPreference", genre)
      }
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