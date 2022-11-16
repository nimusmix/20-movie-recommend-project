<template>
  <div>
    <h1>Login</h1>
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
          this.$store.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(() => {
          this.errMsg = '입력한 정보를 확인해주세요.'
        })
    },
  }
}
</script>
