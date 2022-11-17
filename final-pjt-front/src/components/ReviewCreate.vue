<template>
  <div style="width:500px">
    <h1>ReviewCreate</h1>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
      <div>{{ content.length }}.</div>
      <div>{{ length_warning }}</div>
      {{ content }}
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
      maxlength: 30
    }
  },
  methods:{
    createReview() {
      const content = this.content

      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v2/movies/118/reviews/`,
        data: {
          content: content,
          score:0,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'HomeView' })
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