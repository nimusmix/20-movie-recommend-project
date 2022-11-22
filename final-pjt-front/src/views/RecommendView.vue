<template>
  <div class="router-view-padding">

    <h1 class="h1">{{ username }}님과 비슷한 사용자들이 좋아하는 영화입니다.</h1>
    <div class="row-scroll mb-5">
      <article 
        v-for="movie in recommendSimilar"
        :key="movie.id"
        class="col row-scroll-item"
      >
        <MovieItem :movie="movie"/>
      </article>
    </div>

    <!-- 잠재 모델 -->
    <h1 class="h1">{{ username }}님이 좋아할 만한 영화입니다.</h1>
    <div class="row-scroll mb-5">
      <article 
        v-for="movie in recommendLatent"
        :key="movie.id"
        class="col row-scroll-item"
      >
        <MovieItem :movie="movie"/>
      </article>
    </div>

    <!-- 선호 장르 -->
    <div v-for="(movies, genre, idx) in recommendPreference" :key="idx + 'g'">
      <h1 class="h1">{{ genre }}</h1>
      <div class="row-scroll mb-5">
        <article 
          v-for="movie in movies"
          :key="movie.id"
          class="col row-scroll-item"
        >
          <MovieItem :movie="movie"/>
        </article>
      </div>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'

export default {
  name: 'RecommendView',
  components: {
    MovieItem
  },
  computed: {
    recommendSimilar() {
      return this.$store.state.recommendSimilar
    },
    recommendLatent() {
      return this.$store.state.recommendLatent
    },
    recommendPreference() {
      return this.$store.state.recommendPreference
    },
    username() {
      return this.$store.state.username
    }
  },
}
</script>

<style lang="scss">
  
</style>