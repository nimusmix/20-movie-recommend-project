<template>
  <div>
    <h2>카테고리</h2>
    <div>
      <button
        v-for="genre in genres"
        :key="genre.id"
        @click="genreFilter"
      >
        {{ genre.name }}
      </button>

      <button
        v-for="ott in ottList"
        :key="ott.id"
        @click="ottFilter"
      >
        {{ ott }}
      </button>
    </div>

    <div class="row row-cols-1 row-cols-md-4 g-4">
      <article 
        v-for="movie in movies.filter(movieFilter)"
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
        netflix: '넷플릭스',
        watcha: '왓챠',
        wavve: '웨이브',
        disney: '디즈니',
      },
      selectedGenres: [],
      selectedOtts: [],
    }
  },
  computed: {
    movies(){
      return this.$store.state.movies
    },
    genres(){
      return this.$store.state.genres
    }
  },
  methods: {
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
      console.log(this.selectedGenres)
    },
    ottFilter(event) {
      const ott = event.target.innerText
      const ottEng = Object.keys(this.ottList).find((key) => this.ottList[key] === ott)

      if (this.selectedOtts.includes(ottEng)) {
        const idx = this.selectedOtts.indexOf(ottEng)
        this.selectedOtts.splice(idx, 1)
      } else {
        this.selectedOtts.push(ottEng)
      }
      console.log(this.selectedOtts)
    },
    // movieFilter(movie) {
    //   if (this.selectedGenres.length + this.selectedOtts.length > 0) {
    //     const genreFlag = movie.genres.some((tmpGenre) => this.selectedGenres.includes(tmpGenre))
    //     // const ottFlag = false
    //     if (movie.netflix && selectedOtts.includes('neflix')) {
    //       return true
    //     } elif (movie.watcha && selectedOtts.includes('watcha')) {
    //       return true
    //     } elif (movie.wavve && selectedOtts.includes('waave')) {
    //       return true
    //     }
    //     return genreFlag
    //     }
    //   } else {
    //     return true
    //   }
    // }
  }
}
</script>

<style>

</style>