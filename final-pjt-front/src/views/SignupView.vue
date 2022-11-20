<template>
  <div>
    <h1 class="h1">회원가입</h1>
    <form @submit.prevent="signup">
      <label for="username">이름 : </label>
      <input type="text" id="username" v-model="username"><br>
      <div v-if="usernameErrors">
        <p
          v-for="usernameError in usernameErrors"
          :key="usernameError.id"
        >
          {{ usernameError }}
        </p>
      </div>

      <label for="password1"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>
      <div v-if="password1Errors">
        <p
          v-for="password1Error in password1Errors"
          :key="password1Error.id"
        >
          {{ password1Error }}
        </p>
      </div>

      <label for="password2"> 비밀번호 확인: </label>
      <input type="password" id="password2" v-model="password2" @input="passwordConfirmation">
      <p v-if="password2State">{{ password2State }}</p>
      
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
      password2State: null,
    }
  },
  methods: {
    makePreferences(){
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v3/accounts/make-preferences/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(()=>{
          console.log('[성공] [회원가입] 선호장르 초기화')
        })
        .catch((err)=>{
          console.log('[실패] [회원가입] 선호장르 초기화')
          console.log(err)
        })
    },
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      this.usernameErrors = []
      this.password1Errors = []

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
          // this.$store.dispatch('getLoginUser')
          this.makePreferences()
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
              }
            })
          }
        })
    },
    passwordConfirmation() {
      if (this.password1 !== this.password2) {
        this.password2State = '패스워드가 일치하지 않습니다.'
      } else {
        this.password2State = '패스워드가 일치합니다.'
      }
    }
  },

}
</script>