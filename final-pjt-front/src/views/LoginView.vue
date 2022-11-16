<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>
      <div v-if="usernameErrors">
        <p
          v-for="usernameError in usernameErrors"
          :key="usernameError.id"
        >
          {{ usernameError }}
        </p>
      </div>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>
      <div v-if="passwordErrors">
        <p
          v-for="passwordError in passwordErrors"
          :key="passwordError.id"
        >
          {{ passwordError }}
        </p>
      </div>

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
      usernameErrors: [],
      passwordErrors: [],
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password
      this.usernameErrors = [],
      this.passwordErrors = [],

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
        .catch((err) => {
          console.log('로그인에 실패했습니다.')
          const errData = err.response.data
          console.log(err)
          for (const key in errData) {
            errData[key].forEach((errMsg) => {
              switch(key) {
                case 'username': {
                  this.usernameErrors.push(errMsg)
                  break
                }
                case 'password': {
                  this.passwordErrors.push(errMsg)
                  break
                }
              }
            })
          }
        })
    },
  }
}
</script>
