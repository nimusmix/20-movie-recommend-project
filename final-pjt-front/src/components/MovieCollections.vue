<template>
  <div>
    <h3 class="h3">이 작품이 담긴 컬렉션</h3>
    <div v-for="user in collectedUsers" :key="user.pk" class="user-box" @click="goToProfile(`${user.username}`)">
      <img v-if="user?.profile_img" :src="`http://127.0.0.1:8000${user?.profile_img}`" class="img-circle-100">
      <img v-else src="@/assets/basic.png" class="img-circle-100">
      <p class="mt-2">{{ user.username }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MovieCollections',
  props: {
    movie: Object,
  },
  data() {
    return {
      collectedUsers: [],
    }
  },
  methods: {
    getCollectedUsers() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/collected-users/${this.$route.params.pk}/`
      })
        .then((res) => {
          this.collectedUsers = res.data.user_set
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goToProfile(username) {
      this.$router.push({ name: 'ProfileView', params: { username: username } })
    }
  },
  created() {
    this.getCollectedUsers()
  }
}
</script>

<style>
  .user-box {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    margin-top: 0.4rem;
    margin-right: 2rem;
  }
</style>