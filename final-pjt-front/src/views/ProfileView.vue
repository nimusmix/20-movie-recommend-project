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
          if (this.profileUser?.follwers?.includes(this.loginUser.id)) {
            this.isFollowing = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    follow() {
      this.isFollowing = !this.isFollowing
      let new_followings = this.loginUser.followings
      // console.log(new_followings)
      if (this.isFollowing) {
        new_followings.push(this.profileUser.id)
      } else {
        const idx = new_followings.indexOf(this.profileUser.id)
        new_followings.splice(idx, 1)
      }
      console.log(new_followings)
      const new_data = {
        username: this.loginUser.username,
        follwings: new_followings,
        collection: this.loginUser.collection,
        using_otts: this.loginUser.using_otts,
      }

      axios({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v3/accounts/${this.loginUser.username}/`,
        data: new_data,
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created() {
    this.getProfileUser()
  },
  beforeupdate() {
    this.getProfileUser()
    console.log('ddsf') 
  },
}
</script>

<style>

</style>