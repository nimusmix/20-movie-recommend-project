<template>
  <div class="router-view-padding">

    <div v-if="this.recommendSimilar && this.recommendLatent && this.recommendPreference">
      <!-- 유사 사용자 -->
      <div v-for="recommendObject in recommendSimilar" :key="recommendObject.name">
        <h1 class="h1">{{ recommendObject.label }}</h1>
        <div class="row-scroll mb-5">
          <article 
            v-for="movie in recommendObject.data"
            :key="movie.id"
            class="col row-scroll-item"
          >
            <MovieItem :movie="movie"/>
          </article>
        </div>
      </div>

      <!-- 잠재 모델 -->
      <div v-for="recommendObject in recommendLatent" :key="recommendObject.name">
        <h1 class="h1">{{ recommendObject.label }}</h1>
        <div class="row-scroll mb-5">
          <article 
            v-for="movie in recommendObject.data"
            :key="movie.id"
            class="col row-scroll-item"
          >
            <MovieItem :movie="movie"/>
          </article>
        </div>
      </div>

      <!-- 선호 장르 -->
      <div v-for="recommendObject in recommendPreference" :key="recommendObject.name">
        <h1 class="h1">{{ recommendObject.label }}</h1>
        <div class="row-scroll mb-5">
          <article 
            v-for="movie in recommendObject.data"
            :key="movie.id"
            class="col row-scroll-item"
          >
            <MovieItem :movie="movie"/>
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'RecommendView',
  components: {
    MovieItem
  },
  data() {
    return {
      recommendBaseList: [
        {
          name: 'similar',
          label: '유사 사용자 기반 추천',
          url: 'api/v1/recommend/similar',
        },
        {
          name: 'latent',
          label: '사용자의 장르 기반 잠재 모델 추천',
          url: 'api/v1/recommend/latent',
        },
        {
          name: 'preference',
          label: 'recommend/preference/',
          url: 'api/v1/recommend/preference',
        }
      ],
      recommendSimilar: [],
      recommendLatent: [],
      recommendPreference: [],
      top1List: [],
    }
  },
  methods: {
    getRecommend(recommendObject) {
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

          // 추천 알고리즘의 경우엔 한 개의 영화 리스트를 가져온다.
          if (name === 'similar') {
            this.recommendSimilar.push(temp)
          } else if (name === 'latent') {
            this.recommendLatent.push(temp)
          } else {
            // 선호장르의 경우엔 여러개를 받아오므로 언팩과정을 거친다.
            for (const data of res.data) {
              const temp = {
                label: data.label,
                data: data.movies
              }
              this.recommendPreference.push(temp)
            }
          }
        })
        .catch((err) => {
          console.log(`getRecommend ${name} 실패!`)
          console.log(err)
        })
    },
  },
  created() {
    for (const recommendObj of this.recommendBaseList) {
      this.getRecommend(recommendObj)
    }
  }
}
</script>

<style lang="scss">
  .row-scroll {
    overflow: auto;
    white-space: nowrap;

    .row-scroll-item {
      display: inline-block;
      width: 200px;
      margin-right: 20px;
    }
  }
</style>