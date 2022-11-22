<template>
  <div>
    <h3 class="h3">이 작품이 담긴 컬렉션</h3>
    <div v-for="user in collectedUsers" 
      :key="user.pk" 
      class="user-box cusor-pointer" 
      @click="goToModal(`${user.username}`)">
        <img v-if="user?.profile_img" :src="`http://127.0.0.1:8000${user?.profile_img}`" class="img-circle-100">
        <img v-else src="@/assets/basic.png" class="img-circle-100">
        <p class="mt-2">{{ user.username }}</p>
    </div>
  
    <div v-if="isModalViewed">
      <CollectionModal
        class="collection-modal"
        
        :username="gotoName"
        @close-modal="closeModal"
      />
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import CollectionModal from '@/components/CollectionModal.vue'

export default {
  name: 'MovieCollections',
  props: {
    movie: Object,
    
  },
  components:{
    CollectionModal,
  },
  data() {
    return {
      collectedUsers: [],
      isModalViewed: false,
      gotoName: null,
    }
  },
  methods: {
    openModal() {
      this.isModalViewed = true
    },
    closeModal() {
      this.isModalViewed = false
    },
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
    },
    goToModal(username) {
      this.isModalViewed = true
      this.gotoName = username
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