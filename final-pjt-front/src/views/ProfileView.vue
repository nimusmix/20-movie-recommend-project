<template>
  <div>
    <h1 class="h1">@{{ profileUser?.username }}</h1>
    <div v-if="loginUser.username !== profileUser?.username" @click="follow">
      <button id="followBtn" v-if="isFollowing">언팔로우</button>
      <button id="followBtn" v-else>팔로우</button>
    </div>
    <div>팔로워 {{ profileUser?.followers.length }}</div>
    <div>팔로잉 {{ profileUser?.followings.length }}</div>
    <CollectionList/>
    <collection-modal/>
    <ReviewList/>
  </div>
</template>

<script>
import axios from 'axios'

import CollectionList from '@/components/CollectionList'
import CollectionModal from '@/components/CollectionModal'
import ReviewList from '@/components/ReviewList'

export default {
  name: 'ProfileView',
  components: {
    CollectionList,
    CollectionModal,
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