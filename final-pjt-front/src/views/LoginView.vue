<template>
  <div>
    <h1 class="h1">로그인</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <p v-if="errMsg">{{ errMsg }}</p>
      <input type="submit" value="login">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
      errMsg: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      this.errMsg = null

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        }
      })
        .then((res) => {
          const user = {
            username: this.username,
            token: res.data.key
          }
          this.$store.commit('SAVE_USER', user)
        })
        .then(() => {
          this.$store.dispatch('getLoginUser')
        })
        .catch(() => {
          this.errMsg = '입력한 정보를 확인해주세요.'
        })
    },
  }
}
</script>
