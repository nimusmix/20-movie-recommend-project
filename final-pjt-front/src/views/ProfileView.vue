<template>
  <div>
    <img v-if="profileUser?.profile_img" :src="`http://127.0.0.1:8000${profileUser?.profile_img}`">
    <img v-else src="@/assets/basic.png" alt="">
    <h1 class="h1">@{{ profileUser?.username }}</h1>
    <div>
      <div v-if="loginUser.username !== profileUser?.username" @click="follow">
        <button id="followBtn" v-if="isFollowing">언팔로우</button>
        <button id="followBtn" v-else>팔로우</button>
      </div>
      <router-link
        v-else
        :to="{ name: 'UserEditView', params: { name: 'UserEditView', signUpFlag: 1 } }"
        >
          회원정보수정
        </router-link>
    </div>
    <div class="d-flex">
      <div>팔로워 &nbsp;<b>{{ profileUser?.followers.length }}</b></div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
      <div>팔로잉 &nbsp;<b>{{ profileUser?.followings.length }}</b></div>
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
  },
  created() {
    this.getProfileUser()
  },
}
</script>

<style>

</style>