<template>
  <div style="width: 500px;">
    <h3 class="h3">리뷰 남기기</h3>
    <form id="REVIEW_CREATE" @submit.prevent="createReview">
      <!-- <label for="content">내용 : </label> -->
      <div class="logo" style="position: absolute;">{{ content.length }}.</div>
      <div style="width:2rem; height:2.2rem;"></div>
      <input class="review-input" style="margin-left:4.8rem; width: 380px;" type="text" id="content" cols="30" rows="10" :maxlength='maxlength' :value="content" @click="isStartMethod"  @input="test($event.target.value)"><br>

      <div class="d-flex justify-content-between align-items-center">
        <div style="display: inline-block;">
          <b-form-rating class="star-rating" size="lg" v-model="value"></b-form-rating> 
        </div>
        <div class="d-flex align-items-center">
          <div class="d-flex algin-items-center"><input id="checkbox" type="checkbox" v-model="isSpoiler" >&nbsp;&nbsp;스포일러 포함</div>&nbsp;&nbsp;
          <input type="submit" id="submit" class="main-button selected" style="background-color:#FF715E">
        </div>
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
      content:'리뷰를 입력해주세요.',
      value: 3,
      length_warning: false,
      maxlength: 30,
      isSpoiler: false,
      isStart: false,
    }
  },
  methods:{
    createReview() {
      const content = this.content.substring(0, 20)
      const value = this.value

      if (!content || content==="리뷰를 입력해주세요.") {
        alert('내용을 입력해주세요')
        return
      }

      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v2/movies/${this.$route.params.pk}/reviews/`,
        data: {
          content: content,
          score: value,
          is_spoiler: this.isSpoiler,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // movie detail 받아오기
          axios({
            method: 'get',
            url: `${this.$store.state.API_URL}/api/v1/movies/${res.data.movie}/`
          })
            // movie의 vote_count와 vote_avg 수정
            .then((res) => {
              const now_sum = res.data.vote_average * res.data.vote_count
              const new_sum = now_sum + this.value
              const new_cnt = res.data.vote_count + 1
              const new_avg = Math.round(new_sum / new_cnt * 10) / 10
              const new_data = {
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
                key: res.data.key,
              }
              
              axios({
                method: 'put',
                url: `${this.$store.state.API_URL}/api/v1/movies/${res.data.id}/`,
                data: new_data,
                headers: {
                  Authorization: `Token ${this.$store.state.token}`
                },
              })
                .then(() => {
                  this.$emit('review-created')
                  this.$store.dispatch('getReviews')
                  this.isStart = false
                  this.content = '리뷰를 입력해주세요.'
                })
            })
            .catch((err) => console.log(err))
        })
        .catch((err) => console.log(err))
    },
    test(testinja) {
      this.content = testinja
      if (this.content.length < 20){
        this.length_warning = false
        this.maxlength = 30
      }
      else {
        this.length_warning = true
        setTimeout(() => {
          this.content = this.content.substring(0, 20)
        }, 100);
      }
    },
    isStartMethod(){
      if(this.isStart===false){
        this.isStart=true
        this.content = ''
      }
    }
  },
  computed:{
  }
}

</script>

<style lang="scss">
  #content {
    outline: none;
  }
    
</style>