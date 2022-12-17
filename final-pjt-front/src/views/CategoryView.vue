<template>
  <div class="router-view-padding" ref="scrollcheck">
    <div class="d-flex justify-content-between">
      <h1 class="h1">카테고리</h1>
      <form id="SEARCH-BAR" @submit.prevent="" style="position:relative; cursor: pointer;">
        <!-- stroke="#000000" fill="none" -->
        <svg width="24" height="24" viewBox="0 0 24 24"  xmlns="http://www.w3.org/2000/svg"> 
          <path d="M22 22L20 20M11.5 21C12.7476 21 13.9829 20.7543 15.1355 20.2769C16.2881 19.7994 17.3354 19.0997 18.2175 18.2175C19.0997 17.3354 19.7994 16.2881 20.2769 15.1355C20.7543 13.9829 21 12.7476 21 11.5C21 10.2524 20.7543 9.0171 20.2769 7.86451C19.7994 6.71191 19.0997 5.66464 18.2175 4.78249C17.3354 3.90033 16.2881 3.20056 15.1355 2.72314C13.9829 2.24572 12.7476 2 11.5 2C8.98044 2 6.56408 3.00089 4.78249 4.78249C3.00089 6.56408 2 8.98044 2 11.5C2 14.0196 3.00089 16.4359 4.78249 18.2175C6.56408 19.9991 8.98044 21 11.5 21V21Z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <input type="text" :value="search" class="search-input"  @input="searchUpdate($event.target.value)" @focus="focusSearch(true)" @blur="focusSearch(false)">
        <b-list-group v-show="isFocusSearch" style="position:absolute; top:32px; left: 24px; z-index: 9;">
          <b-list-group-item class="flex-column align-items-start" v-for="searchResult in searchResults" :key="searchResult.id">
            <div @mousedown="goDetail(searchResult.id)" class="d-flex justify-content-between">
              <h5 class="mb-1">{{ searchResult.title }}</h5>
              <!-- <h5 class="mb-1">{{ searchResult.id }}</h5> -->
            </div>
          </b-list-group-item>
        </b-list-group>
      </form>
      
    </div>
    
    
    
    

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
      </article>
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem'
import axios from 'axios'


export default {
  name: 'CategoryView',
  components: {
    MovieItem,
  },
  data() {
    return {
      search:"검색하기",
      visibleIdx: 100,
      ottList: {
        watcha: '왓챠', 
        waave: '웨이브',
        disney: '디즈니',
        netflix: '넷플릭스',
      },
      selectedOtts: [],
      selectedGenres: [],
      searchResults: [],
      isFocusSearch: false,
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
    goDetail(movieId){
      // console.log(movieId)
      this.$router.push({ name: 'DetailView', params: { pk: movieId } })
    },
    focusSearch(act){
      this.isFocusSearch = act
      if (this.search == '검색하기'){
        this.search = ''
      }else if (this.search == ''){
        this.search = '검색하기'
      }
    },
    searchUpdate(event){
      this.search = event
      if (this.search.length >= 2){
        axios({
          method: 'get',
          url: `${this.$store.state.API_URL}/api/v1/movies-search/${event}/`,
        })
          .then((res) => {
            // console.log('검색요청!')
            this.searchResults = res.data
            this.searchResults.forEach((result, index)=>{
              this.searchResults[index]["index"] = this.$store.state.movieIdIndex[result.id]
            })
            // console.log(this.searchResults)
          })
          .catch(() => {
            // console.log('검색요청실패!')
          })
      }
      else{
        this.searchResults = []
      }
      
    },
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
      // console.log(this.$refs.scrollcheck.scrollHeight)
      // console.log(window.innerHeight)
      // console.log(window.scrollY)
      if ( this.$refs.scrollcheck.scrollHeight - (window.innerHeight + window.scrollY) < 1000){
        this.visibleIdx += 100
      }
    }
  },
  created() {
    this.selectedOtts = this.$store.state.selectedOtts
    this.selectedGenres = this.$store.state.selectedGenres
    this.visibleIdx = this.$store.state.visibleIdx
    window.addEventListener("scroll", this.handleScroll)
  },
  beforeDestroy() {
    const data = {
      selectedOtts: this.selectedOtts,
      selectedGenres: this.selectedGenres,
      visibleIdx: this.visibleIdx,
    }
    this.$store.commit('SAVE_CATEGORY', data)
    window.removeEventListener('scroll', this.handleScroll);
  },
}
</script>

<style lang="scss">
#SEARCH-BAR{
  height: 32px;
  border: 0;
  border-radius: 15px;
  outline: none;
  padding-left: 10px;
  background-color: var(--bg-color);
  svg{
    stroke: var(--text-color);
    fill:none;
    width:16px;
    height: 16px;
  }
  .search-input{
    height: 32px;
    border: 0;
    border-radius: 15px;
    outline: none;
    padding-left: 5px;
    background-color: var(--bg-color);
    color: var(--text-color);
  }

}
  /* .button-list {
    display: flex;
    flex-wrap: wrap;
  } */

  .movie-count {
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
  }
</style>