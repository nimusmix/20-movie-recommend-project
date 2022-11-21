<template>
  <div>
    <h1 class="h1">회원정보수정</h1>
    <div>
      <input type="file" @change="changeImg" ref="profileImg">
    </div>

    <div class="button-list">
      <button
        v-for="perference in perferences" :key="perference.genre.id"
        :class="[{'selected': perference.like}, 'main-button']"
        @click="isSelectedGenre(perference)">
        {{ perference.genre_name }}
      </button>
    </div>

    <div v-if="this.$route.params.signUpFlag === '1'">
      <form @submit.prevent="editInfo('HomeView', false)">
        <button>건너뛰기</button>
      </form>
      <form @submit.prevent="editInfo('HomeView', true)">
        <button>가입완료</button>
      </form>
    </div>

    <div v-else>
      <form @submit.prevent="editInfo('ProfileView', false)">
        <button>수정취소</button>
      </form>
      <form @submit.prevent="editInfo('ProfileView', true)">
        <button>수정하기</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserEditView',
  data() {
    return {
        perferences: null,
        img: null,
    }
  },
  methods: {
  // 선호 장르를 받아온다.
    getPerferences() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/perferences/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then((res) => {
          console.log('1 actions의 editInfo 성공!')
          this.perferences = res.data
        })
        .catch((err) => {
          console.log('actions의 editInfo 실패!')
          console.log(err)
        })
    },
    changeImg() {
      this.img = this.$refs.profileImg.files[0]
    },
    editProfileImg() {
      axios({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v3/accounts/edit-profile-img/`,
        data: {
          'profile_img': this.img,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
          'Content-Type': 'multipart/form-data',
        },
      })
        .then((res) => {
          console.log(res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 선호 장르 수정
    editPreferences() {
      for (const perference of this.perferences) {
        axios({
          method: 'put',
          url: `${this.$store.state.API_URL}/api/v3/accounts/edit-perferences-like/${perference.genre}/`,
          data: {
              'like': perference.like,
          },
          headers: {
              Authorization: `Token ${this.$store.state.token}`
          },
        })
          // .then(() => {
          //   console.log(`${perference.genre} editPreferences 성공!`)
          // })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    // editOtts() {
      
    // },
    // 회원 정보 수정
    editInfo(nextPage, is_axios) {
        // 1은 회원가입 후를 
      if (is_axios) {
        this.editProfileImg()
        this.editPreferences()
        // this.editOtts()
      }

      if (nextPage === 'HomeView') {
        this.$router.push({ name: nextPage })
      } else if (nextPage === 'ProfileView') {
        this.$router.push({ name: nextPage, params: { username: this.username } })
      }
    },
    genreCheck(event) {
      event.target.innerText
    },
    isSelectedGenre(perference) {
      const idx = this.perferences.indexOf(perference)
      this.perferences[idx].like = !this.perferences[idx].like
    },
  },
  computed:{
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.getPerferences()
  },
}
</script>

<style>

</style>