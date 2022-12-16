<template >
  <div class="router-view-padding" ref="scrollcheck">
    <h1 class="h1">카테고리</h1>
    <div class="button-list">
      <button
        v-for="ott in otts"
        :key="ott.id"
        :class="[{'selected': isSelectedOtt(ott)}, 'main-button']"
        @click="ottFilter"
      >
        {{ ottList[ott.name] }}
      </button>

      <button 
        v-for="genre in genres"
        :key="genre.id"
        :class="[{'selected': isSelectedGenre(genre)}, 'main-button']"
        @click="genreFilter"
      >
        {{ genre.name }}
      </button>
    </div>

    <p class="movie-count">{{ filteredMovies.length }}개의 영화가 있습니다.</p>
    <div class="row row-cols-1 row-cols-md-4 row-cols-xl-6 g-4">
      <article 
        v-for="movie in filteredMovies.slice( 0, visibleIdx )"
        :key="movie.id"
        class="col"
      >
        <MovieItem :movie="movie"/>
        <!-- <div class="movie-card">
          <a class="t-d-none">
            <div  style="position:relative">
              <div class="card-img-top" style="background-color:gray" alt="..."></div>
            </div>
            <h5 class="movie-card-title">{{   }}</h5>
            <div class="movie-card-detail">{{   }}</div>
            <p class="movie-card-detail"><span>로딩 중... </span> </p>
          </a>
        </div> -->
      </article>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'



export default {
  name: 'CategoryView',
  components: {
    MovieItem,
  },
  data() {
    return {
      visibleIdx: 100,
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
      } else {
        return false
      }
    },
    isSelectedGenre(genre) {
      if (this.selectedGenres.includes(genre.id)) {
        return true
      } else {
        return false
      }
    },
    handleScroll() {
      if ( this.$refs.scrollcheck.scrollHeight - (window.innerHeight + window.scrollY) < 1000){
        this.visibleIdx += 100
      }
    }
  },
  created() {
    this.selectedOtts = this.$store.state.selectedOtts
    this.selectedGenres = this.$store.state.selectedGenres
    this.visibleIdx = this.$store.state.visibleIdx
  },
  beforeDestroy() {
    const data = {
      selectedOtts: this.selectedOtts,
      selectedGenres: this.selectedGenres,
      visibleIdx: this.visibleIdx,
    }
    this.$store.commit('SAVE_CATEGORY', data)
  },
  updated(){
    window.addEventListener("scroll", this.handleScroll)
  }
}
</script>

<style>
  /* .button-list {
    display: flex;
    flex-wrap: wrap;
  } */

  .movie-count {
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
  }
</style>