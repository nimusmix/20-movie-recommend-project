<template>
  <div>
    <div class="overlay" @click="closeModal">
    
    </div>
    <div id="MODAL" class="modal-card">
      <div class="center-head">
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
      </div>
      <h3 class="h3">{{ profileUser?.username }}님의 컬렉션</h3>
      <!-- {{ collections }} -->
      <div v-for="collection, index in collections" :key="index">
        <MovieItemVue :movie="collection" class="modal-movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieItemVue from '@/components/MovieItem'

export default {
  name: 'CollectionModal',
  components: {
    MovieItemVue
  },
  data(){
    return{
      profileUser: null,
      isFollowing: false,
    }
  },
  props: {
    collections: Array,
  },
  methods: {
    closeModal() {
      this.$emit('close-modal')
    },
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
  #MODAL{
    border-radius: 8px;
  }
  .overlay {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 2;
    background-color: black;
  }

  .modal-card{
   -ms-overflow-style: none;
  }
  /* 임의의 영역 생성 */
  .scrollBar { 
    width: 200px;
    height: 200px;
    overflow-y: scroll;
    overflow-x: none;
  }
  
  /* 아래의 모든 코드는 영역::코드로 사용 */
  .modal-card::-webkit-scrollbar {
    width: 10px;  /* 스크롤바의 너비 */
  }

  .modal-card::-webkit-scrollbar-thumb {
      height: 5%; /* 스크롤바의 길이 */
      background: var(--primary-color); /* 스크롤바의 색상 */
      border-radius: 10px;
  }

  .modal-card::-webkit-scrollbar-track {
      background: var(--primary-color-10);  /*스크롤바 뒷 배경 색상*/
      margin-top:50px;
      margin-bottom:50px;
      border-radius: 10px;
  }


  .modal-card {
    /* position: relative; */
    height: 70%;
    position: fixed;
    width: 70%;
    top: 15%;
    left: 15%;
    
    margin-left: auto;
    margin-right: auto;
    z-index: 3;
    overflow:scroll;
    padding: 20px;
    background-color: white;
    /* border: 1px red solid; */
  }

  .modal-movie{
    width: 200px;
  }

  .center-head{
    display: flex;
    justify-content: center;
    margin: 2rem 0px;
  }
</style>