<template>
  <div>
    <div class="overlay" @click="closeModal">
    
    </div>
    <div id="MODAL" class="modal-card">

      <div class="center-head">
        <div class="head-box">
          <div class="profile-img-box">
            <img class="img-circle-100" v-if="profileUser?.profile_img" :src="`${$store.state.API_URL}${profileUser?.profile_img}`">
            <img class="img-circle-100" v-else src="@/assets/basic.png" alt="">
          </div>
          <div class="detail-box">
            <div class="user-and-button" >
              <h1 class="h1 m-0">@{{ profileUser?.username }}</h1>
              <div class="space"></div>
              <div v-if="loginUser.username !== profileUser?.username" @click="follow">
                <button class="r-main-button selected" v-if="flag">팔로우 중</button>
                <button class="r-main-button" v-else>팔로우하기</button>
              </div>
            </div>
            <div class="follow-info">
              <div>팔로워 &nbsp;<b>{{ profileUser?.followers.length }}</b></div>
              <div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
              <div>팔로잉 &nbsp;<b>{{ profileUser?.followings.length }}</b></div>
            </div>
          </div>
        </div>
      </div>
      <h3 class="h3">&nbsp;&nbsp;{{ profileUser?.username }}님의 컬렉션</h3>

      <div style="position:relative">
        <button @click="scrollRight('rowMovies')" class="row-scroll-button r-s-b-left">
          <svg stroke="#FFF" fill="none" width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M17.9998 12.0001V14.6701C17.9998 17.9801 15.6498 19.3401 12.7798 17.6801L10.4698 16.3401L8.15982 15.0001C5.28982 13.3401 5.28982 10.6301 8.15982 8.97005L10.4698 7.63005L12.7798 6.29005C15.6498 4.66005 17.9998 6.01005 17.9998 9.33005V12.0001Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </button>
        <button @click="scrollLeft('rowMovies')" class="row-scroll-button r-s-b-right">
          <svg stroke="#FFF" fill="none"  width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 12.0002V9.33017C6 6.02017 8.35 4.66017 11.22 6.32017L13.53 7.66017L15.84 9.00017C18.71 10.6602 18.71 13.3702 15.84 15.0302L13.53 16.3702L11.22 17.7102C8.35 19.3402 6 17.9902 6 14.6702V12.0002Z"  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        </button>
        <div class="row-scroll mb-5" :ref="'rowMovies'">
          <article 
            v-for="movie, index in profileUser?.collection" :key="index"
            class="col row-scroll-item"
          > 
            <MovieItem :movie="movie" class="modal-movie"/>
          </article>
        </div>
      </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItem from '@/components/MovieItem'

export default {
  name: 'CollectionModal',
  components: {
    MovieItem
  },
  data(){
    return{
      profileUser: null,
      flag: false,
      leftIcon : '<',
      rightIcon : '>',
    }
  },
  props:{
    username: String,
  },
  methods: {
    scrollRight(idx){
      const move = parseInt(this.$store.state.width / 2)
      this.$refs[idx].scrollBy({ left: -move, behavior: 'smooth' });
    },
    scrollLeft(idx){
      const move = parseInt(this.$store.state.width / 2)
      this.$refs[idx].scrollBy({ left: move , behavior: 'smooth' });
    },
    closeModal() {
      this.$emit('close-modal')
    },
    getProfileUser() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v3/accounts/${this.username}/`,
      })
      .then((res) => {
        this.profileUser = res.data
      })
      .then(() => {
        
        this.isFollowing()
      })
      .catch((err) => {
        console.log(err)
      })
    },
    follow() {

      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v3/accounts/follow/${this.profileUser.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.$store.dispatch('getLoginUser')
          this.getProfileUser()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    isFollowing() {
      this.flag = false
      
      this.profileUser.followers.forEach((following)=>{
          if (following.username===this.loginUser.username){
            this.flag = true
          }
      })
    },
    goToEdit() {
      this.$router.push({ name: 'UserEditView', params: { name: 'UserEditView', signUpFlag: 0 } })
    }
  },
  computed:{
    loginUser() {
      return this.$store.state.loginUser
    },
    width(){
      return this.$store.state.width
    },
    height(){
      return this.$store.state.height
    }
  },
  created() {
    this.getProfileUser()
  },
}
</script>

<style>
  
</style>
