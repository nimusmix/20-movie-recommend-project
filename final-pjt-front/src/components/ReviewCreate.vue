<template>
  <div style="width:500px">
    <h1>ReviewCreate</h1>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
      <div>{{ content.length }}.</div>
      <div>{{ length_warning }}</div>                         <!-- 확인 -->
      <input id="content" cols="30" rows="10" :maxlength='maxlength' :value="content" @input="test($event.target.value)"><br>
      <input type="submit" id="submit">
      <div style="width:100%">
        <b-form-rating v-model="value" color="#ff8800" show-value></b-form-rating>
        <p class="mt-2">Value: {{ value }}</p>
      </div>


    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreate',
  data(){
    return{
      content:'Default Message',
      value: 3,
      length_warning: false,
      maxlength: 30,
    }
  },
  methods:{
    createReview() {
      const content = this.content.substring(0, 20)
      const value = this.value
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v2/movies/${this.$route.params.pk}/reviews/`,
        data: {
          content: content,
          score: value,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          axios({                                                          // movie detail 받아오기
            method: 'get',
            url: `${this.$store.state.API_URL}/api/v1/movies/${res.data.movie}/`
          })
            .then((res) => {                                               // movie의 vote_count와 vote_avg 수정
              const now_sum = res.data.vote_average * res.data.vote_count
              const new_sum = now_sum + this.value
              const new_cnt = res.data.vote_count + 1
              const new_avg = new_sum / new_cnt
              axios({
                method: 'put',
                url: `${this.$store.state.API_URL}/api/v1/movies/${res.data.id}/`,
                data: {
                  title: res.data.title,
                  overview: res.data.overview,
                  release_date: res.data.release_date,
                  popularity: res.data.popularity,
                  adult: res.data.adult,
                  vote_count: new_cnt,
                  vote_average: new_avg,
                  backdrop_path: res.data.backdrop_path,
                  poster_path: res.data.poster_path,
                  original_language: res.data.original_language,
                  original_title: res.data.original_title,
                  genres: res.data.genres,
                  otts: res.data.otts,
                },
                headers: {
                  Authorization: `Token ${this.$store.state.token}`
                },
              })
        })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    test(testinja){
      this.content = testinja
      if (this.content.length < 20){
        this.length_warning = false
        this.maxlength = 30
      }
      else{
        this.length_warning = true
        setTimeout(() => {
          console.log("after")
          this.content = this.content.substring(0, 20)
          console.log(this.content)
        }, 100);
      }
    }
  },
  computed:{
  }
}

</script>

<style>

</style>