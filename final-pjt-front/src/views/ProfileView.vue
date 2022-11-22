<template>
  <div class="router-view-padding">

    <div class="head-box">
      
      <div class="profile-img-box">
        <img class="img-circle-100" v-if="profileUser?.profile_img" :src="`http://127.0.0.1:8000${profileUser?.profile_img}`">
        <img class="img-circle-100" v-else src="@/assets/basic.png" alt="">
      </div>
      <div class="detail-box">

        <div class="user-and-button">
          <h1 class="h1 m-0">@{{ profileUser?.username }}</h1>
          <div class="space"></div>
          <div v-if="loginUser.username !== profileUser?.username" @click="follow">
            <button id="followBtn" class="main-button selected" v-if="isFollowing">언팔로우</button>
            <button id="followBtn" class="main-button selected" v-else>팔로우</button>
          </div>
          <button v-else class="main-button selected" @click="goToEdit">회원정보수정</button>
        </div>
        <div class="follow-info">
          <div>팔로워 &nbsp;<b>{{ profileUser?.followers.length }}</b></div>
          <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
          <div>팔로잉 &nbsp;<b>{{ profileUser?.followings.length }}</b></div>
        </div>
      </div>
    </div>
    <div class="space"></div>
    <CollectionList :collection="profileUser?.collection"/>
    <div class="space"></div>
    <ReviewList/>
  </div>
</template>

<script>
import axios from 'axios'

import CollectionList from '@/components/CollectionList'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'ProfileView',
  components: {
    CollectionList,
    ReviewList,
  },
  data() {
    return {
      profileUser: null,
      isFollowing: false,
    }
  },
  computed: {
    loginUser() {
      return this.$store.state.loginUser
    },
  },
  methods: {
    getProfileUser() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/${this.$route.params.username}/`,
      })
      .then((res) => {
        this.profileUser = res.data
      })
      .then(() => {
        if (this.loginUser.followings.includes(this.profileUser.id)) {
          this.isFollowing = true
        }
      })
      .catch((err) => {
        console.log(err)
      })
    },
    follow() {
      this.isFollowing = !this.isFollowing

      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v3/accounts/follow/${this.profileUser.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.getProfileUser()
          this.$store.dispatch('getLoginUser')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goToEdit() {
      this.$router.push({ name: 'UserEditView', params: { name: 'UserEditView', signUpFlag: 0 } })
    }
  },
  created() {
    this.getProfileUser()
  },
}
</script>

<style lang="scss">
  

</style>