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
      // let new_followings = this.loginUser.followings

      if (this.isFollowing) {
        // 포스트맨에서는 됨 ,, 이렇게 보내면 안 됨.. 대체 왜 ,,,
        // 근데 팔로잉 여러 명 하는 거 안 됨 지금..!!! 자꾸 하나만 됨 ..
        axios({
          method: 'put',
          url: `${this.$store.state.API_URL}/api/v3/accounts/${this.loginUser.username}/follow`,
          data: {
            username: this.loginUser.username,
            followings: this.profileUser.id,
            // collection: this.loginUser.collection,
            // genre_preference: this.loginUser.genre_preference,
            // using_otts: this.loginUser.using_otts,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
          .then((res) => {
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        // 언팔 아직 구현 안함..
        // axios delete로 구현하면 될 듯!
      }

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