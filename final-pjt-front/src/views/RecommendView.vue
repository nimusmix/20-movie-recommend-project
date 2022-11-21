<template>
  <div>
    <h1 class="h1">추천영화</h1>
    <div v-for="recommendObject in recommendBaseList" :key="recommendObject.name">
      <button @click="getRecommend(recommendObject)">{{ recommendObject.name }}</button>
    </div>
    <div v-for="recommendObject in recommendResults" :key="recommendObject.name">
      <div>
        {{ recommendObject.label }}
      </div>
      <div class="row row-cols-1 row-cols-md-4 g-4">
        <article 
          v-for="movie in recommendObject.data"
          :key="movie.id"
          class="col"
        >
        <MovieItem :movie="movie"/>
        </article>
      </div>
    </div>
    
    <RecommendList />
  </div>
</template>

<script>
import axios from 'axios'
import RecommendList from '@/components/RecommendList'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'RecommendView',
  components: {
    RecommendList,
    MovieItem
  },
  data(){
    return{
      recommendBaseList:[
        {
          name: 'latent',
          label: '사용자의 장르기반 잠재모델 추천',
          url: 'api/v1/recommend/latent',
        }
      ],
      recommendResults:[]
    }
  },
  methods: {
    getRecommend(recommendObject){
      const {name, label, url} = recommendObject
      axios({
          method: 'get',
          url: `${this.$store.state.API_URL}/${url}/`,
          headers: {
              Authorization: `Token ${this.$store.state.token}`
          },
      })
          .then((res) => {
            console.log(`getRecommend ${name} 성공!`)
            const temp = {
              label: label,
              data: res.data
            }
            this.recommendResults.push(temp)
          })
          .catch((err) => {
            console.log(`getRecommend ${name} 실패!`)
            console.log(err)
          })
    },
    getTest(){
      
    },
  }
}
</script>

<style>

</style>