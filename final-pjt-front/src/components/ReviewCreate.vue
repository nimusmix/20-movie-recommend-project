<template>
  <div style="width:500px">
    <h1>ReviewCreate</h1>
    <form id="REVIEW_CREATE" @submit.prevent="createReview">
      <!-- <label for="content">내용 : </label> -->
      <div class="logo">{{ content.length }}.</div>
      <!-- <div>{{ length_warning }}</div>                         확인 -->
      <input id="content" cols="30" rows="10" :maxlength='maxlength' :value="content" @input="test($event.target.value)"><br>
      
      <div style="display:inline-block">
        <b-form-rating class="star-rating" size="lg" v-model="value"></b-form-rating> 
      </div>
      <!-- show-value -->
      <input id="checkbox" type="checkbox" v-model="is_spoiler"> 스포일러 포함
      
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreate',
  data(){
    return{
      content:'내용을 입력해주세요',
      value: 3,
      length_warning: false,
      maxlength: 30,
      is_spoiler: false,
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
          is_spoiler: this.is_spoiler,
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
              }

              axios({
                method: 'put',
                url: `${this.$store.state.API_URL}/api/v1/movies/${res.data.id}/`,
                data: new_data,
                headers: {
                  Authorization: `Token ${this.$store.state.token}`
                },
              })

              location.reload()                      // 페이지 새로고침하는 코드. DetailView에 리뷰 출력 기능 구현 후 리뷰 작성 시 페이지 업데이트 된다면
          })                                         // 여기서 reload 하지 말고 DetailView updated()로 movie 데이터 업데이트하기
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
    },
    test2() {
      console.log(this.is_spoiler)
    }
  },
  computed:{
  }
}

</script>

<style lang="scss">
    #REVIEW_CREATE {
      border: 1px solid var(--text-color);
      padding: 1rem 1.5rem ;
      background: var(--bg-color);
      border-radius: 8px;
      border-color: var(--primary-color);
      box-shadow: 0px 0px 10px 0px var(--primary-color-15);
      .logo{
        display: inline-block;
      }
      input{
        color: var(--disable-color);
        background-color: none;
        border: none;
      }
    }
    .b-rating{
      margin: 0px;
      padding: 0px;
    }
    .star-rating{
      background-color: none;
      border: none;
      
      .b-rating-star{
        margin: 0px;
        padding: 4px;
      }
      .b-rating-icon{
        color: var(--primary-color);
        margin: 0px;
        padding: 0px;
        svg{
          min-width:1px;
        }
      }
    }
</style>