<template>
  <div>
    <h1 class="h1">회원가입</h1>
    <form @submit.prevent="signup">
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

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <div v-if="password1Errors">
        <p
          v-for="password1Error in password1Errors"
          :key="password1Error.id"
        >
          {{ password1Error }}
        </p>
      </div>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      <div v-if="password2Errors">
        <p
          v-for="password2Error in password2Errors"
          :key="password2Error.id"
        >
          {{ password2Error }}
        </p>
      </div>
      
      <input type="submit" value="Signup">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      usernameErrors: [],
      password1Errors: [],
      password2Errors: [],
    }
  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      this.usernameErrors = [],
      this.password1Errors = [],
      this.password2Errors = [],

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
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
        .catch((err) => {
          console.log('회원가입에 실패했습니다.')
          const errData = err.response?.data
          for (const key in errData) {
            errData[key].forEach((errMsg) => {
              switch(key) {
                case 'username': {
                  this.usernameErrors.push(errMsg)
                  break
                }
                case 'password1': {
                  this.password1Errors.push(errMsg)
                  break
                }
                case 'password2': {
                  this.password2Errors.push(errMsg)
                  break
                }
              }
            })
          }
        })
    }
  },

}
</script>