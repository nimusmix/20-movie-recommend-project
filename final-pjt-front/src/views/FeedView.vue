<template>
  <div>
    <h1>FeedView</h1>
    <FeedItem/>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import FeedItem from '@/components/FeedItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'FeedView',
  components: {
    FeedItem,
  },
  data(){
    return{
      content:null,
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
        url: `${API_URL}/api/v2/movies/118/reviews/`,
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
    }
  }
}
</script>

<style>

</style>