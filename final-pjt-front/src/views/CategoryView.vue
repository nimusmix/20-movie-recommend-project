<template>
  <div>
    <h1 class="h1">카테고리</h1>
    <div>
      <button
        v-for="ott in otts"
        :key="ott.id"
        :class="{'selected': isSelectedOtt(ott)}"
        @click="ottFilter"
      >
        {{ ottList[ott.name] }}
      </button>

      <button
        v-for="genre in genres"
        :key="genre.id"
        :class="{'selected': isSelectedGenre(genre)}"
        @click="genreFilter"
      >
        {{ genre.name }}
      </button>
    </div>

    <p>{{ filteredMovies.length }}개의 영화가 있습니다.</p>
    <div class="row row-cols-1 row-cols-md-4 g-4">
      <article 
        v-for="movie in filteredMovies"
        :key="movie.id"
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
  data() {
    return {
      ottList: {
        watcha: '왓챠',
        waave: '웨이브',
        disney: '디즈니',
        netflix: '넷플릭스',
      },
      selectedOtts: [],
      selectedGenres: [],
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    otts() {
      return this.$store.state.otts
    },
    genres() {
      return this.$store.state.genres
    },
    filteredMovies() {
      return this.$store.state.movies.filter(this.movieFilter)
    }
  },
  methods: {
    ottFilter(event) {
      const ott = event.target.innerText
      const ottEng = Object.keys(this.ottList).find((key) => this.ottList[key] === ott)

      for (const tmpOtt of this.otts) {
        if (tmpOtt.name === ottEng) {
          const id = tmpOtt.id
          if (this.selectedOtts.includes(id)) {
            const idx = this.selectedOtts.indexOf(ott)
            this.selectedOtts.splice(idx, 1)
          } else {
            this.selectedOtts.push(id)
          }
          break
        }
      }
    },
    genreFilter(event) {
      const genre = event.target.innerText
      for (const tmpGenre of this.genres) {
        if (tmpGenre.name === genre) {
          const id = tmpGenre.id

          if (this.selectedGenres.includes(id)) {
            const idx = this.selectedGenres.indexOf(genre)
            this.selectedGenres.splice(idx, 1)
          } else {
            this.selectedGenres.push(id)
          }
          break
        }
      }
    },
    movieFilter(movie) {
      let ottFlag = true
      let genreFlag = true

      if (this.selectedOtts.length) {
        ottFlag = this.selectedOtts.every((selectedOtt) => movie.otts.includes(selectedOtt))
      }
      if (this.selectedGenres.length) {
        genreFlag = this.selectedGenres.every((selectedGenre) => movie.genres.includes(selectedGenre))
      }
      return ottFlag && genreFlag
    },
    isSelectedOtt(ott) {
      if (this.selectedOtts.includes(ott.id)) {
        return true
      } else{
        return false
      }
    },
    isSelectedGenre(genre) {
      if (this.selectedGenres.includes(genre.id)) {
        return true
      } else{
        return false
      }
    },
  },
}
</script>

<style>
  .selected {
    background-color: red;
  }
</style>